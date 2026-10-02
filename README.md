# Eurekaimer

[![Website](https://img.shields.io/badge/website-eurekaimer.icu-b91c1c?style=flat-square)](https://www.eurekaimer.icu/)
[![Astro](https://img.shields.io/badge/Astro-6.4-BC52EE?style=flat-square&logo=astro&logoColor=white)](https://astro.build/)
[![CI](https://img.shields.io/github/actions/workflow/status/Eurekaimer/Eurekaimer.github.io/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/Eurekaimer/Eurekaimer.github.io/actions/workflows/ci.yml)
[![Deploy](https://img.shields.io/github/actions/workflow/status/Eurekaimer/Eurekaimer.github.io/deploy.yml?branch=main&style=flat-square&label=Pages)](https://github.com/Eurekaimer/Eurekaimer.github.io/actions/workflows/deploy.yml)

The source of my personal homepage, [www.eurekaimer.icu](https://www.eurekaimer.icu/). It is a small front door to my notes, projects, and interests, built with [Astro](https://astro.build/) and adapted from [AstroPaper](https://github.com/satnaing/astro-paper).

## Why Astro

I considered [Hugo](https://gohugo.io/), [MkDocs](https://www.mkdocs.org/), and [Jekyll](https://jekyllrb.com/) before choosing Astro.

- **Hugo** is exceptionally fast and well suited to conventional blogs, but Astro gives me a more familiar component model for shaping a distinctive homepage.
- **MkDocs** remains an excellent choice for structured notes and documentation, which is why my notes live separately. A personal homepage, however, needs more freedom in layout and presentation.
- **Jekyll** integrates naturally with GitHub Pages, but Astro offers a more modern TypeScript-based workflow and a broader component ecosystem.
- **Astro** keeps the final site mostly static while allowing interactive features only where they are useful. That balance makes the site fast, maintainable, and easy to personalize.

AstroPaper provides a restrained foundation; the content, visual identity, and page structure are customized for this site.

## Site map

| Site                                       | Purpose                            |
| ------------------------------------------ | ---------------------------------- |
| [Main site](https://www.eurekaimer.icu/)   | Profile, projects, and links       |
| [Notes](https://www.eurekaimer.icu/notes/) | Study notes and reference material |

## Editing the site

Page sources live directly in the root-level `pages/` directory. Astro uses the repository root as `srcDir`; `src/` holds the internal implementation, not route entry points.

```text
pages/
  index.astro       Homepage
  about.md          Personal biography and website introduction
  cv.md             Academic CV
  friends.astro     Friends and link exchange
  showcase.astro    Gallery
  404.astro         Not-found page
  robots.txt.ts     Robots endpoint
src/
  styles/           Fonts, typography, theme, and page-specific CSS
  layouts/          Shared document and Markdown-page layouts
  components/       Navigation and reusable UI
  scripts/          Client-side behavior
  content/posts/    Article content
  assets/           Imported images and icons
  utils/            Internal helpers
public/             Static images and domain configuration
content.config.ts   Astro content collections
```

Edit `pages/about.md` and `pages/cv.md` directly; their shared layout supplies the page title, navigation, and footer. The CV contains education, research interests, awards, skills, and CET-6, without GPA or coursework. The USTC M.S. entry is marked **planned**, September 2027–June 2030; update that status when appropriate. Its organization follows the identity, education, research-interest, and honors sections of [Jeffrey N. Jonkman's academic CV](https://www.grinnell.edu/sites/default/files/Jonkman%20CV.pdf), with personal facts drawn from the supplied CV and subsequent profile updates.

Public pages use the pseudonym Eurekaimer and the site's public contact mailbox, including SEO descriptions. Notes links point to `/notes/`; this site does not link to the separate personal blog.

Skills include Linux, Java, and Go; both profile pages list AI infrastructure, large language models, and distributed systems among the research interests. The homepage's Japanese image caption stays on one line with responsive font sizing in `src/styles/home.css`.

### Typography

Fonts are self-hosted through Fontsource; no runtime font CDN is required.

- H1: Libertinus Serif Italic, large; navigation links keep their regular style.
- H2/H3: Libertinus Serif Italic, progressively smaller.
- H4–H6 and body: Libertinus Serif Regular.
- All headings use weight 400; hierarchy comes from size, margins, and line height.
- Strong and emphasized body text use the real italic face, not bold.
- Code, preformatted text, keyboard input, and sample output use JetBrains Mono.
- `font-synthesis: none` prevents synthetic bold and italic.

Font imports are in `src/styles/fonts.css`, family tokens in `src/styles/theme.css`, and hierarchy rules in `src/styles/typography.css`.

`src/styles/global.css` imports the font faces, theme, and typography as one shared stylesheet. `Layout.astro` loads its processed Vite `?url` asset with a `<link rel="stylesheet">`; the client router retains that loaded asset across pages instead of replacing it with cached development-time inline CSS. This keeps heading styles consistent during navigation without a manual refresh, while production still compiles Tailwind and bundles the font assets.

## Development

```bash
pnpm install
pnpm run dev --host 0.0.0.0 --port 8001
```

Open [http://localhost:8001/](http://localhost:8001/), [About](http://localhost:8001/about/), or [Academic CV](http://localhost:8001/cv/).

Before publishing, run:

```bash
pnpm run lint
pnpm run format:check
pnpm run build
```

The site is deployed to [GitHub Pages](https://pages.github.com/) through [GitHub Actions](https://github.com/features/actions).

## License

The AstroPaper-derived theme code is available under the [MIT License](LICENSE). Original writing and media remain the property of their respective authors unless otherwise stated.
