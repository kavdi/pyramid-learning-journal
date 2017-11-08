"""Configut and hold all pertenent security information for the app."""

import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Everyone, Authenticated, Allow
from passlib.apps import custom_app_context as pwd_context


class MyRoot(object):
    """Set class for MyRoot to set what views need authorization."""

    def __init__(self, request):
        """Set settings for views available with and without authorization."""
        self.request = request

    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'secret'),
    ]


def security_check(username, password):
    """Check if the user's username and password are good."""
    if username == os.environ.get('AUTH_USERNAME', ''):
        if pwd_context.verify(password, os.environ.get('AUTH_PASSWORD', '')):
            return True
    return False


def includeme(config):
    """security-related configuration."""
    auth_secret = os.environ.get('AUTH_SECRET', '')
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg='sha512'
    )
    config.set_authentication_policy(authn_policy)
    # add the following new lines of configuration and the new import above.
    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
    config.set_default_permission('view')
    config.set_root_factory(MyRoot)
