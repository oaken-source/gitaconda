
from pyramid.view import view_config, view_defaults
from pyramid.renderers import get_renderer
from pyramid.interfaces import IBeforeRender
from pyramid.events import subscriber


@subscriber(IBeforeRender)
def globals_factory(event):
    event['master'] = get_renderer('gitaconda_server:templates/master.pt').implementation()
    event['base_anon'] = get_renderer('gitaconda_server:templates/base_anon.pt').implementation()
    event['base_auth'] = get_renderer('gitaconda_server:templates/base_auth.pt').implementation()



@view_config(route_name='index', renderer='gitaconda_server:templates/index.pt')
def index(request):
    return {}
