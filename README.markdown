# Snippets

Simply Django app to map named snippets to content for insertion in templates
via a {% snippet %} tag.

## How To Use

Add `'snippets'` to `INSTALLED_APPS` and run `syncdb`. Then, add any named
snippets you wish from the admin console. In any template, simply load the
snippets tag library via

    {% load snippet_tags %}

and insert the snippet anywhere you wish with

    {% snippet "the-snippet-name" %}

If `settings.DEBUG` is true, a warning about missing snippets will be inserted,
but nothing will be inserted in production if a snippet is missing.
