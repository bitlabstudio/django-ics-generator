"""URL patterns for the ``ics_generator`` app."""
from django.conf.urls import url, patterns

from .views import ICSView


urlpatterns = patterns(
    '',
    url(r'^event.ics$',
        ICSView.as_view(),
        name='ics_generator'),
)
