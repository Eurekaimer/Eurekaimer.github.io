# Eurekaimer

This repository contains the main site for [www.eurekaimer.icu](https://www.eurekaimer.icu/). It uses [AstroPaper](https://github.com/satnaing/astro-paper) as a minimal Astro-based personal homepage.

The old MkDocs digital garden has been split into smaller sites:

- Main Site: <https://www.eurekaimer.icu/>
- Notes: <https://www.eurekaimer.icu/Stathelper/>
- Focus on life blog: <https://www.eurekaimer.icu/blog/>

## Why AstroPaper

AstroPaper was chosen for two main reasons:

**Minimalism.** The theme keeps the site lightweight — no heavy frameworks, no unnecessary JavaScript. Pages are static HTML by default, with JavaScript only where truly needed (theme toggle, Giscus comments). This means fast load times and a clean reading experience.

**Separation of concerns.** Content and presentation are cleanly separated:
- **Content** lives in `src/content/` as Markdown files (e.g., `about.md`), editable without touching any component code.
- **Configuration** is centralized in `astro-paper.config.ts` — site metadata, social links, feature toggles are all in one place.
- **Layout & components** in `src/layouts/` and `src/components/` handle the presentation layer. Shared pieces (Header, Footer, Socials) are reused across all pages.
- **Pages** in `src/pages/` are thin Astro components that compose layouts and content together.

This structure makes the site easy to maintain: change a social link in config, edit about text in a markdown file, tweak the homepage layout in `index.astro` — each concern has a single, obvious home.

## Development

Install dependencies and start the local server:

```bash
pnpm install
pnpm run dev
```

Build locally:

```bash
pnpm run build
```

Preview the production build:

```bash
pnpm run preview
```

## Deployment

This site is intended to deploy with GitHub Pages and GitHub Actions.

Repository settings to confirm on GitHub:

- Settings -> Pages -> Source: GitHub Actions
- Custom domain: `www.eurekaimer.icu`
- DNS: the `www` CNAME record should point to `Eurekaimer.github.io`

After checking the build locally, publish with:

```bash
git add .
git commit -m "Migrate main site to AstroPaper"
git push origin main
```

## License

Original writing is shared under CC BY-SA 4.0 where applicable. AstroPaper is distributed under its own license; see `LICENSE` for the theme license included in this repository.
