# Contributing

Open an issue for a bug or a proposal. Include the page, viewport, browser, and steps to reproduce. For a pull request, keep changes focused and describe how you tested them. Do not submit personal data or third-party assets without permission to redistribute them.

Run `bundle exec ruby tests/check_data.rb`, `bundle exec jekyll build` and `python3 tests/check_site.py _site`. Also build with `--baseurl /example-site` and check it using `python3 tests/check_site.py _site /example-site`. Check the layout at desktop and phone widths before proposing visual changes.
