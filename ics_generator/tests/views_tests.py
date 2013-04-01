"""Tests for the views of the ``ics_generator`` app."""
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.test import RequestFactory, TestCase

from ..views import ICSView


class ICSViewTestCase(TestCase):
    """Tests for the ``GetCTypeDetails`` view class."""
    longMessage = True

    def test_view(self):
        req = RequestFactory().get('/')
        req.GET = {'content': 'BEGIN%3AVCALENDAR%0AVERSION%3A2.0%0APRODID%3Ajquery.icalendar%0AMETHOD%3APUBLISH%0ABEGIN%3AVEVENT%0AUID%3A1364815856688@localhost%3A8000%0ADTSTAMP%3A20130401T113056Z%0AURL%3Ahttp%3A//localhost%3A8000/en/events/1/%0ATITLE%3AA%20Test%20Event%0ADTSTART%3A20130531T220000Z%0ADTEND%3A20130604T040000Z%0ASUMMARY%3AA%20Test%20Event%0ADESCRIPTION%3AWorkshop%0ALOCATION%3AA%20Venue%20Name%20Wuppertal%2C%20Germany%0AEND%3AVEVENT%0AEND%3AVCALENDAR', }  # NOQA
        resp = ICSView.as_view()(req)
        self.assertTrue('BEGIN' in resp.content, msg=(
            'Should return a .ics file as a attachment download'))
