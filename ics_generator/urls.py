"""URL patterns for the ``ics_generator`` app."""
from django.conf.urls.defaults import url, patterns

from .views import ICSView


urlpatterns = patterns(
    '',
    # About Advisors
    url(r'^event.ics$',
        ICSView.as_view(),
        name='ics_generator'),
)
