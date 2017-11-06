
"""Test default.py."""
from pyramid.testing import DummyRequest
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.models.meta import Base
from learning_journal.models.mymodel import MyModel
from pyramid import testing
import pytest
FMT = '%m/%d/%Y'


@pytest.fixture(scope='session')
def configuration(request):
    """Set up a Configurator instance."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://localhost:5432/test_learning_journal'
    })
    config.include("learning_journal.models")
    config.include("learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture(scope='session')
def db_session(configuration, request):
    """Create a session for interacting with the test database."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope='session')
def dummy_request(db_session):
    """Instantiate a fake HTTP Request, complete with a database session."""
    return testing.DummyRequest(dbsession=db_session)


def test_list_view_returns_list_of_journals_in_dict(dummy_request):
    """Test if list view returns dictionary with word 'title'."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


# def test_journal_exists(dummy_request):
#     from learning_journal.views.default import list_view
#     new_entry = MyModel(
#         id=11,
#         title='Something Awesome',
#         creation_date=datetime.strptime("11/02/2017", FMT),
#         body='Some random letters and what not.'
#     )
#     dummy_request.dbsession.add(new_entry)
#     dummy_request.dbsession.commit()
#     response = list_view(dummy_request)
#     assert new_entry.to_dict() in response['posts']
