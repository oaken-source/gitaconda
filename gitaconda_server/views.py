
from pyramid.view import view_config, view_defaults


@view_defaults(renderer='templates/hello.pt')
class HelloViews(object):

    def __init__(self, request):
        self.request = request

    @view_config(route_name='hello_set')
    def hello_set(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        self.request.session['last'] = last
        self.request.session['first'] = first
        return { 'first': first, 'last': last }

    @view_config(route_name='hello')
    def hello(self):
        first = self.request.session['first']
        last = self.request.session['last']
        return { 'first': first, 'last': last }
