""" Ye olde hello world sanity check, using only the base template.

Purpose: ensure we can process the request to render a simple template
Author: Tom W. Hartung
Date: Winter, 2017
Copyright: (c) 2017 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
    Chapter 3 of the "Flask Web Development" book (M.Grinberg 2014)
Usage:
    bin/hello-run.sh
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/home')
def home():

    """ Render the home.html template """

    return render_template('home.html', home_active='is-active')


@app.route('/about')
def about():

    """ Render the about.html template """

    #include_deleted_blah_blah = False
    include_deleted_blah_blah = True

    return render_template(
        'about.html',
        about_active='is-active',
        include_deleted_blah_blah=include_deleted_blah_blah
    )


@app.route('/blog')
def blog():

    """ Render the blog.html template """

    return render_template('blog.html', blog_active='is-active')


@app.route('/portfolio')
def portfolio():

    """ Render the portfolio.html template """

    return render_template('portfolio.html', portfolio_active='is-active')


@app.route("/legal/<legal_page>")
def legal(legal_page):

    """ Display the requested legal page, defaulting to the terms_of_service """

    if legal_page == 'privacy_policy':
        template_name = 'legal/privacy_policy.html'
    elif legal_page == 'terms_of_service':
        template_name = 'legal/terms_of_service.html'
    elif legal_page == 'affiliate_marketing_disclosure':
        template_name = 'legal/affiliate_marketing_disclosure.html'
    else:
        template_name = 'legal/terms_of_service.html'

    return render_template(template_name, legal_active='is-active')


@app.route('/index')
def index():

    """ Render the index.html template """

    return render_template('index.html')


@app.route('/v')
def versions():
    """ Show the versions.html template to see what versions we are using """

    import platform
    python_version = platform.python_version()
    import flask
    flask_version = flask.__version__

    template_name = 'versions.html'
    return render_template(
        template_name,
        python_version=python_version,
        flask_version=flask_version
    )


@app.errorhandler(404)
def page_not_found(e):

    """
    Handle 404 errors by showing the 404.html template
    Found this code here:
        http://flask.pocoo.org/docs/0.12/patterns/errorpages/
    """

    return render_template('404.html'), 404


# =============================================================================

#
# Run the app!
#
if __name__ == '__main__':
    app.run(debug=True)
