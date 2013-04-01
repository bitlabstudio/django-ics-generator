Django ICS Generator 
====================

A simple Django view that returns a .ics file as an attachment download when
called via the icalendar script: http://www.keith-wood.name/icalendar.html

Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django

If you want to install the latest stable release from PyPi::

    $ pip install django-ics-generator

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-ics-generator.git#egg=ics_generator

Add ``ics_generator`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'ics_generator',
    )

Include the urls for this app::

    urlpatterns = patterns(
        '',
        url(r'^ics-generator/', include('ics_generator.urls')),
    )


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-ics-generator
    $ pip install -r requirements.txt
    $ ./logger/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
