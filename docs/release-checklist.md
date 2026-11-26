# Academic homepage template: release checklist

The template is a separate Jekyll site derived from the design of the author's academic homepage and based on al-folio. This document describes the release requirements, not features already installed in this repository. Never modify or deploy the author's original site as part of this release.

## Scope

- Keep the desktop sidebar, compact mobile navigation, warm light and dark palettes, profile header, and research/publication layout. Keep the first release focused; omit the sidebar arcade.
- Use one editable research-area data file to group BibTeX entries and select representative papers on the homepage. Include a small collection of clearly fictional examples for biography, publications, projects, and news. Include a generic avatar and an original or explicitly redistributable sample figure.
- Keep the template self-contained. Move name, tagline, contact links, profile image, and metadata into configuration. Use GitHub Pages-compatible relative URLs for both a user site and a repository subpath.
- Copy only the intended source files into this repository. Do not import the personal repository's Git history, CV, portraits, paper PDFs or figures, real publication records, submission details, contacts, analytics/site-verification identifiers, domain settings, local credentials, or internal notes. Scan the files, generated output, and the history of this repository before release.

## Open-source files

- Match MIT notices to the actual upstream revisions used. The personal repository's LICENSE credits Michael Rose, and al-folio publishes its own MIT notice. Preserve all applicable notices and record provenance and asset licenses in THIRD_PARTY_NOTICES.md. Use replacement assets where redistribution rights cannot be established.
- Add a README with screenshots, a quick start, exact configuration paths, local preview steps, and GitHub Pages deployment, plus CONTRIBUTING.md with test and contribution instructions. Do not imply affiliation with al-folio or promise support terms that are not offered.

## Release acceptance

1. Build from a clean clone on CI with the documented Ruby and locked dependencies. Check generated links and research-group references. Build and test both root and project-subpath configurations.
2. Check desktop and mobile layouts, keyboard navigation, the mobile menu, theme switching, and a representative publication link. No personal data should appear in the demo or screenshots.
3. Keep draft CI build-only until release. Verify that the template and demo actually work independently of the original site. Only then set this repository to public, enable GitHub's template setting, and verify the public demo and Use this template flow.
4. Xiaohongshu is out of scope for this release.
