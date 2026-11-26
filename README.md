# Academic Homepage Template

A restrained research homepage for GitHub Pages. It pairs a desktop sidebar and a compact mobile header with a publication catalog: update one research-area file, and the homepage and publication groups stay in sync.

[Open the live demo](https://h20zhang.github.io/academic-homepage-template/). It uses fictional content throughout. This is a slim adaptation of an academic site built on [al-folio](https://github.com/alshedivat/al-folio), not a drop-in upstream theme.

## Quick start

1. On GitHub, click **Use this template**. Name your new repository `USERNAME.github.io` for a user site, or choose any other name for a project site.
2. Edit the files below. Remove any fictional items you don't need.
3. Go to **Settings → Pages**, set **Source** to **GitHub Actions**, then run **Build and deploy** from the **Actions** tab with **Run workflow**. The deployment uses the base URL reported by GitHub Pages. Pull requests build and check the site without deploying.

| Change | Edit |
| --- | --- |
| Name, bio, optional native name, portrait, links | `_data/profile.yml` |
| Research groups and homepage highlights | `_data/research_areas.yml` |
| Paper metadata and links | `_bibliography/papers.bib` |
| Project cards and news | `_data/projects.yml`, `_data/news.yml` |
| Default palette | `appearance_palette` in `_config.yml` |
| Custom colors and layout | `assets/css/site.css` |

Use unique BibTeX keys, assign each listed paper to one research group, and use only keys from that group for its homepage highlights. Add a paper's `url` or `doi` when available.

## Appearance

Choose Warm Stone, Ocean, Forest, Lilac, Ink, or High Contrast. Each palette has light and dark variants. The site follows the device's light/dark preference until the visitor selects a mode. It remembers palette and mode locally. To set the default for new visitors, change `appearance_palette` in `_config.yml`.

## Local preview

Install Ruby 3.3 and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000`. To verify the production build, run `bundle exec ruby tests/check_data.rb`, `bundle exec jekyll build` and `python3 tests/check_site.py _site`. For a project-site path, build with `--baseurl /example-site` and run `python3 tests/check_site.py _site /example-site`.

## License

MIT. See [LICENSE](LICENSE), [third-party notices](THIRD_PARTY_NOTICES.md), and [contribution instructions](CONTRIBUTING.md). Your own site content and assets remain subject to their respective rights.
