
"""Test default.py."""
from pyramid.testing import DummyRequest
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.models.meta import Base
from learning_journal.models.mymodel import MyModel
from pyramid import testing
import pytest


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


def dummy_request(db_session):
    """Instantiate a fake HTTP Request, complete with a database session."""
    return testing.DummyRequest(dbsession=db_session)


# Tests start here
def test_list_view_returns_list_of_journals_in_dict(dummy_request):
    """Test if list view returns dictionary with word 'title'."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_returns_empty_dict_with_no_entered_data(dummy_request):
    """Test if list view returns dictionary with nothing in it if empty."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert len(response['post']) == 0


def test_list_view_contains_new_data_added(dummy_request):
    """Test if data sent through the request is added to the db."""
    from learning_journal.views.default import list_view
    new_post = MyModel(
        title='The real struggle',
        author='bobby',
        date=datetime.now(),
        text='Once upon a time.. there was a test!'
    )
    dummy_request.dbsession.add(new_post)
    dummy_request.dbsession.commit()
    response = list_view(dummy_request)
    assert new_post.to_dict() in response['post']


def test_detail_view_returns_dict(dummy_request):
    """Test if detail view returns dictionary."""
    from learning_journal.views.default import detail_view
    new_post = MyModel(
        title='The great struggle',
        author='bobby',
        date=datetime.now(),
        text='Once upon a time.. there was another test!'
    )
    dummy_request.dbsession.add(new_post)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 1
    response = detail_view(dummy_request)
    assert isinstance(response, dict)


def test_detail_view_returns_sinlgle_item(dummy_request):
    """Test if detail view returns dictionary with contents of 'title'."""
    from learning_journal.views.default import detail_view
    new_post = MyModel(
        title='The beast',
        author='bobby',
        date=datetime.now(),
        text='Once upon a time.. a big bad test!'
    )
    dummy_request.dbsession.add(new_post)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 2
    response = detail_view(dummy_request)
    assert response['post']['title'] == 'The beast'


def test_detail_view_raises_not_found_if_id_not_found(dummy_request):
    """Test if detail raises HTTPNotFound if id not in dict."""
    from learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 100
    with pytest.raises(HTTPNotFound):
        detail_view(dummy_request)


def test_create_view_returns_dict(dummy_request):
    """Test if create view returns a dictionary."""
    from learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert isinstance(response, dict)


def test_create_view_returns_empty_dict(dummy_request):
    """Test if create view returns a dictionary."""
    from learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert len(response) == 0


def test_update_view_returns_dict(dummy_request):
    """Test if update view returns a dictionary."""
    from learning_journal.views.default import update_view
    new_post = MyModel(
        title='The update',
        author='bobby',
        date=datetime.now(),
        text='fix what needs fixin!'
    )
    dummy_request.dbsession.add(new_post)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 1
    response = update_view(dummy_request)
    assert isinstance(response, dict)


def test_update_view_returns_title_of_single_entry(dummy_request):
    """Test if update view title of single item chosen."""
    from learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 2
    response = update_view(dummy_request)
    assert response['post']['title'] == 'The update'


def test_update_view_raises_exception_id_not_found(dummy_request):
    """Test if update raises exception on non-existent id."""
    from learning_journal.views.default import update_view
    dummy_request.matchdict['id'] = 100
    with pytest.raises(HTTPNotFound):
        update_view(dummy_request)
