
# joomoowebsites.com

Replacing the joomla site with flask.  Time to move on.

# Goal

- Very simple site
- Flask and MDL

# Resources

## MDL CSS and JS

- Download MDL V1.3.0 as `mdl.zip` from:
  - https://getmdl.io/started/index.html
  - Saved in this repo as `Downloads/mdl.zip`
  - Using **only** the following files from the .zip file:
    - `material.css` as `static/css/material.1.3.0.css-for_reference_only`
    - `material.min.js` as `static/js/material.min.js`
    - `material.min.js.map` as `static/js/material.min.js.map`
    - `LICENSE` as `static/LICENSE-MDL.txt`

## Colors

- Download blue-red material.min.css from:
  - https://getmdl.io/customize/index.html
  - Saved in this repo as `Downloads/material-blue-red.min.css`
  - Using it as `static/css/material-blue-red.min.css`
- Color picker, used to generate the blue-red.min.css file:
  - https://getmdl.io/customize/index.html
- Material Design Color Palettes:
  - https://material.io/design/color/#tools-for-picking-colors

## JQuery

- Download jquery 3.3.1 from:
  - https://jquery.com/download/
  - Using it as `static/jquery-3.3.1.min.js`

## Templates

Inspired by code previously downloaded into the `always_learning_google_products` repo:

- 1. Navigation, about, blog portfolio pages based on examples downloaded:
  - `material_design/08-mdl/02-portfolio/Site/about.html` in `always_learning_google_products`
  - `material_design/08-mdl/02-portfolio/Site/blog.html` in `always_learning_google_products`
  - `material_design/08-mdl/02-portfolio/Site/index.html` in `always_learning_google_products`
- 2. Home page - try to use "blog" template
  - `material_design/08-mdl/01-blog/Site/index.html` in `always_learning_google_products`

Specific files used from `always_learning_google_products`:

- `material_design/08-mdl/02-portfolio/Site/styles.css` as `css/styles.css`
  - Later: renamed `css/styles.css` to `css/joomoowebsites.css`
- `material_design/08-mdl/01-blog/Sitestyles.css` as `css/styles-home.css`

**NOTE:**

- The paths for image files are defined in `css/joomoowebsites.css`

## Process

Framework - Core Files

- Downloaded and renamed as described above

Templates

- Used markup from `material_design/08-mdl/02-portfolio/Site` as appropriate

# Disappointments

Having looked through the documentation, I am not seeing a way to do the
following things, which are features that other MD libraries support:

- Drop-down sub-menus
- Centering text
- Footer wants to have left and right sides, I want it centered and in the middle
- Documentation is poor, e.g., does not have a list of colors
  - For a list of colors, grep for `mdl-color-text-` in the css file
  - Ref: https://stackoverflow.com/questions/36668356/is-there-a-html-class-for-changing-text-color-in-material-design-lite

I could furnish css to do these things, but feel like I shouldn't have to.

# Notes

## Cruft Alerts!

- Legal pages copied from groja.com, still have some MDB styles left in them

# Content Ideas

- "Simple Sites Built With Python and Material Design"
- Target - possibly on home page, possibly under the fold:
  - Small business
  - Looking for more than Wix
  - Not wanting to use WP for some reason
    - Concerned about security
    - It is frequently overkill
  - Want a shiny new MD look
- Pricing - possibly on home page, possibly under the fold:
  - Value-based
  - Weekly invoice or half up front
  - Incremental, frequent deliveries and corresponding payments
- Portfolio: page listing other Python + MD sites
- Legal pages
- Why page/option - instead of About
  - Decide:
  - Option 1: Keep it minimal
    - Maybe include photo of JooMoo Tree?
    - Maybe just point to tomwhartung.com?
  - Option 2: Tell the whole story
    - Similar to About page on Groja.com
    - Explain reasons for and difficulties faced in giving up php for python
