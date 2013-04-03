"""Views for the ``hero_slider`` app."""
from django.views.generic import View
from django.http import Http404, HttpResponse


class ICSView(View):
    """Returns a download with an .ics file for the given GET data."""
    http_method_names = [u'get', ]

    def get(self, request, *args, **kwargs):
        content = request.GET.get('content')
        response = HttpResponse(content, content_type='text/calendar')
        response['Content-Disposition'] = 'attachment; filename=event.ics'
        return response
