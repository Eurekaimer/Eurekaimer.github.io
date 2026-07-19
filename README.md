# Eurekaimer

[![Website](https://img.shields.io/badge/website-eurekaimer.icu-b91c1c?style=flat-square)](https://www.eurekaimer.icu/)
[![Astro](https://img.shields.io/badge/Astro-6.4-BC52EE?style=flat-square&logo=astro&logoColor=white)](https://astro.build/)
[![CI](https://img.shields.io/github/actions/workflow/status/Eurekaimer/Eurekaimer.github.io/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/Eurekaimer/Eurekaimer.github.io/actions/workflows/ci.yml)
[![Deploy](https://img.shields.io/github/actions/workflow/status/Eurekaimer/Eurekaimer.github.io/deploy.yml?branch=main&style=flat-square&label=Pages)](https://github.com/Eurekaimer/Eurekaimer.github.io/actions/workflows/deploy.yml)

The source of my personal homepage, [www.eurekaimer.icu](https://www.eurekaimer.icu/). It is a small front door to my notes, daily writing, projects, and interests, built with [Astro](https://astro.build/) and adapted from [AstroPaper](https://github.com/satnaing/astro-paper).

## Why Astro

I considered [Hugo](https://gohugo.io/), [MkDocs](https://www.mkdocs.org/), and [Jekyll](https://jekyllrb.com/) before choosing Astro.

- **Hugo** is exceptionally fast and well suited to conventional blogs, but Astro gives me a more familiar component model for shaping a distinctive homepage.
- **MkDocs** remains an excellent choice for structured notes and documentation, which is why my notes live separately. A personal homepage, however, needs more freedom in layout and presentation.
- **Jekyll** integrates naturally with GitHub Pages, but Astro offers a more modern TypeScript-based workflow and a broader component ecosystem.
- **Astro** keeps the final site mostly static while allowing interactive features only where they are useful. That balance makes the site fast, maintainable, and easy to personalize.

AstroPaper provides a restrained foundation; the content, visual identity, and page structure are customized for this site.

## Site map

| Site                                            | Purpose                               |
| ----------------------------------------------- | ------------------------------------- |
| [Main site](https://www.eurekaimer.icu/)        | Profile, projects, and links          |
| [Notes](https://www.eurekaimer.icu/Stathelper/) | Study notes and reference material    |
| [Daily blog](https://www.eurekaimer.icu/blog/)  | Informal writing and everyday records |

## Development

```bash
pnpm install
pnpm run dev
```

Before publishing, run:

```bash
pnpm run lint
pnpm run format:check
pnpm run build
```

The site is deployed to [GitHub Pages](https://pages.github.com/) through [GitHub Actions](https://github.com/features/actions).

## License

The AstroPaper-derived theme code is available under the [MIT License](LICENSE). Original writing and media remain the property of their respective authors unless otherwise stated.
