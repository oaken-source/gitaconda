
from pyramid_beaker import session_factory_from_settings
from pyramid.config import Configurator


def main(global_config, **settings):
    session_factory = session_factory_from_settings(settings)
    config = Configurator(settings=settings)
    config.set_session_factory(session_factory)

    config.include('pyramid_chameleon')
    config.include('pyramid_beaker')
    config.include('pyramid_tm')
    config.include('pyramid_sqlalchemy')

    config.add_route('index', '/')

    config.add_static_view(name='static', path='gitaconda_server:static')
    config.scan('.views')

    return config.make_wsgi_app()
