# Chris' Startupify Demo

## Introduction

This is a very simple beer database with reviews (single-user, created via
the admin intervace) and commenting (multi-user, unauthenticated commenting
via the public web interface). I built it do explore Django and to use as a
demo submission for [Startupify](http://startupify.me/).

## Some general notes

- The application supports multiple reviews per beer by design.
- The commenting is pretty sparse since most of the code is pretty standard
  Django-type stuff. I don't believe in documenting the framework within my
  code unless something is really weird.

## Running the demo

The demo has only been tested with Django 1.3.1, the built-in development
server and SQLite on Python 2.7.2.

I believe that simply cloning the repository will be sufficient to get this
up and running if you've already got Django installed. The standard

    python manage.py runserver

should get you up and running. If you have trouble, please let me know.

If you check out the `master` branch you will not have any data. Create the
database as usual with

    python manage.py syncdb

and then start adding data using the admin interface.

If you prefer to start with some sample data, check out the `data`
branch. This includes an existing SQLite database and some images in the
`media/` directory. The superuser account is `chris` / `startupify`.

## Some things that I used

Pretty much everything from the Django tutorial is in here, but I played with
some additional features as well:

- Model metadata using inner `Meta` classes.
- Template inheritance using the `extends` keyword.
- Static files to serve up my CSS and my uploaded media files.
- Custom template filter to generate "SEO friendly" link tails.

## Some things that I'd consider adding going forward

- Searching, by integrating an existing Django search app.
- Tagging of reviews via the admin interface, and a tag cloud.
- Markdown support for review bodies and comments.

## Some things that I'd fix if this was a real site

- The front-end design is pretty utilitarian. Attention from a designer would
  be nice. Having said that, I spent most of my time on the Django stuff; if
  necessary I could make some improvements to the HTML/CSS/JavaScript portion
  as well.
- Fix the empty, grey-outlined sidebar div shown on pages where the sidebar
  isn't used (e.g. the Beer view).
- Make sure that comments only save if both fields are filled out.
- Re-evaluate the generation of tail links. The custom filter that I wrote
  was a good experiment, but it looks like the `permalink` decorator might be
  a better option.
