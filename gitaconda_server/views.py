
from pyramid.view import view_config, view_defaults
from pyramid.renderers import get_renderer
from pyramid.interfaces import IBeforeRender
from pyramid.events import subscriber


@subscriber(IBeforeRender)
def globals_factory(event):
    base = get_renderer('gitaconda_server:templates/base.pt').implementation()
    event['base'] = base


@view_config(route_name='index', renderer='gitaconda_server:templates/index.pt')
def index(request):
    return {}
