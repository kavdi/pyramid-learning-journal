"""."""
from pyramid import testing


def dummy_request(dbsession):
    """Create a dummy request to the server."""
    return testing.DummyRequest(dbsession=dbsession)
