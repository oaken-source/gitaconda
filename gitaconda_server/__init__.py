
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()
