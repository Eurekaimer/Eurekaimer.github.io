/**
 * Umami Cloud stats proxy for the blog footer.
 *
 * Turns the Umami Cloud API key into a small, edge-cached JSON endpoint so the
 * key never reaches the browser:
 *
 *   GET /api/umami-stats  →  { "pageviews": 12345, "visitors": 3210 }
 *
 * Env bindings (see wrangler.toml):
 *   UMAMI_API_KEY     secret, set with `npx wrangler secret put UMAMI_API_KEY`
 *   UMAMI_WEBSITE_ID  plain var, falls back to the constant below
 */

/** Umami Cloud API base (v1 — verified: /v1 routes exist, /api do not). */
const UMAMI_API_BASE = "https://api.umami.is/v1";

/** Website being counted. Server-side constant — the key is the secret, not this. */
const DEFAULT_WEBSITE_ID = "a30cfbd2-8c6d-48f2-aeb6-e6297914ac2c";

/**
 * Start of the recorded history. The footer claims the blog has been running
 * since 2024-10-28, so the start of 2024 covers every recorded visit.
 */
const START_AT = Date.UTC(2024, 0, 1);

/** ~1h edge cache, serve stale while revalidating behind the scenes. */
const CACHE_CONTROL = "public, s-maxage=3600, stale-while-revalidate=86400";

export default {
  async fetch(request: Request, env: Record<string, string | undefined>) {
    const url = new URL(request.url);

    if (request.method !== "GET") {
      return new Response("Method Not Allowed", { status: 405 });
    }
    if (url.pathname !== "/api/umami-stats") {
      return new Response("Not Found", { status: 404 });
    }

    const websiteId = env.UMAMI_WEBSITE_ID ?? DEFAULT_WEBSITE_ID;
    if (!env.UMAMI_API_KEY) {
      return new Response(
        JSON.stringify({ error: "UMAMI_API_KEY is not configured" }),
        { status: 500, headers: { "content-type": "application/json" } }
      );
    }

    const upstream = await fetch(
      `${UMAMI_API_BASE}/websites/${websiteId}/stats?startAt=${START_AT}&endAt=${Date.now()}`,
      { headers: { authorization: `Bearer ${env.UMAMI_API_KEY}` } }
    );

    // Never cache errors — return them as-is so the footer can hide quietly.
    if (!upstream.ok) {
      return new Response(JSON.stringify({ error: "upstream stats failed" }), {
        status: upstream.status,
        headers: { "content-type": "application/json" },
      });
    }

    const data = (await upstream.json()) as {
      pageviews?: number;
      visitors?: number;
    };

    return new Response(
      JSON.stringify({
        pageviews: data.pageviews ?? 0,
        visitors: data.visitors ?? 0,
      }),
      {
        status: 200,
        headers: {
          "content-type": "application/json",
          "cache-control": CACHE_CONTROL,
          // Harmless on the same-origin custom-domain route; needed if the
          // worker is ever hit through a workers.dev URL instead.
          "access-control-allow-origin": "*",
        },
      }
    );
  },
};
