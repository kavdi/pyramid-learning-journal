"""."""
from pyramid.testing import DummyRequest
import pytest


@pytest.fixture
def req():
    """Create a dummy GET request."""
    return DummyRequest()


def test_home_list_view_shows_list_of_titles_in_dict(req):
    from learning_journal.views.default import list_view
    response = list_view(req)
    assert 'posts' in response
    assert isinstance(response['posts'], list)


def test_home_lists_view_includes_title(req):
    from learning_journal.views.default import list_view
    response = list_view(req)
    assert 'title' in response['posts'][0]


def test_edit_lists_view_includes_title(req):
    from learning_journal.views.default import update_view
    req.matchdict['id'] = 2
    response = update_view(req)
    assert 'title' in response['post']


def test_view_includes_post_title(req):
    from learning_journal.views.default import detail_view
    req.matchdict['id'] = 3
    response = detail_view(req)
    assert 'Day 3' in response['post']['title']


def test_creat_view_includes_post_title(req):
    from learning_journal.views.default import create_view
    response = create_view(req)
    assert isinstance(response, dict)


@pytest.fixture
def testapp():
    from webtest import TestApp
    from pyramid.config import Configurator

    def main():
        config = Configurator()
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
        return config.make_wsgi_app()

    app = main()
    return TestApp(app)


def test_home_route_has_h4_titles(testapp):
    from learning_journal.data.blog_post import POSTS
    response = testapp.get("/")
    assert len(POSTS) == len(response.html.find_all('h4'))


def test_detail_view_route_has_text(testapp):
    response = testapp.get("/journal/9")
    print(response.html)
    assert "cookiecutter... pyramids...deques..." in str(response.html)


def test_update_view_has_an_submit_button(testapp):
    response = testapp.get("/update/2")
    assert len(response.html.find_all('button', attrs={"type": "submit"})) == 1
    assert "Submit" in response.html.find('button', attrs={"type": "submit"})


def test_create_view_has_a_submit_button(testapp):
    response = testapp.get("/create")
    assert len(response.html.find_all('button', attrs={"type": "submit"})) == 1
    assert "Submit" in response.html.find('button', attrs={"type": "submit"})
