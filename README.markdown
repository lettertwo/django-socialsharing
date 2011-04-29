Socialsharing
=============
This project is a simple integration of various social sharing services for 
quick integration into Django projects. The list of supported sharing services 
follows:

addthis
=======
The addthis templatetag will insert the necessary scripts to make use of the 
[AddThis](https://www.addthis.com) widget.

Basic usage:
------------

    {% addthis pubid=xxxxxxxxxx %}

or with `ADDTHIS_PUBID` defined in settings.py:

    {% addthis %}

The only required argument is `pubid`. You may optionally provide a 
global setting for this by adding `ADDTHIS_PUBID = xxxxxx` 
to your settings.py. Setting this value means that you can omit the `pubid` 
argument when invoking the templatetag.

Optional settings:
------------------
`share_url`: The url to share. Pass this argument to override the default 
AddThis value (the URL of the page being viewed). Example:

    {% addthis 'http://myurl.com' %}

`track_clickback`: From the AddThis docs:

    Set to true to allow us to append a variable to your URLs upon sharing. 
    We'll use this to track how many people come back to your content via links 
    shared with AddThis. Highly recommended.

default value is `True`.  
**Note:** You may optionally set 
`ADDDTHIS_TRACK_CLICKBACK = False` to always force this value to `False`.

To enable tracking via Google Analytics:
----------------------------------------
* add `ADDTHIS_GA_TRACKING_ENABLED = True` to your settings.py
* add `ADDTHIS_GA_TRACKER = UA-XXXXXX-X` to your settings.py

**Note:** If you don't set `ADDDTHIS_GA_TRACKER`, the template tag will attempt to 
fall back to `GA_TRACKING_CODE` (which is used by 
[Django-HTML5Boilerplate](http://github.com/matthewwithanm/django-html5boilerplate)).
