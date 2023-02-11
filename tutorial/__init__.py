from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.set_security_policy(SecurityPolicy())
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.include('.models')
        config.scan()
    return config.make_wsgi_app()


class SecurityPolicy:
    def identity(self, request):
        raise NotImplementedError()  # pragma: no cover

    def authenticated_userid(self, request):
        return 1

    def permits(self, request, context, permission):
        raise NotImplementedError()  # pragma: no cover

    def remember(self, request, userid, **kw):
        raise NotImplementedError()  # pragma: no cover

    def forget(self, request, **kw):
        raise NotImplementedError()  # pragma: no cover
