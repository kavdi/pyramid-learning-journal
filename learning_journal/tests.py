"""."""
import pytest
from pyramid import testing
from learning_journal.views.default import (
    list_view,
    detail_view,
    create_view,
    update_view
)


@pytest.fixture
def dummy_request():
    """Create a dummy request to the server."""
    return testing.DummyRequest()


def test_list_view_response_status_code_200_ok(dummy_request):
    """Test if request will return 200 ok response."""
    response = list_view(dummy_request)
    assert response.status_code == 200


def test_datail_view_response_status_code_200_ok(dummy_request):
    """Test if request will return 200 ok response."""
    response = detail_view(dummy_request)
    assert response.status_code == 200


def test_create_view_response_status_code_200_ok(dummy_request):
    """Test if request will return 200 ok response."""
    response = create_view(dummy_request)
    assert response.status_code == 200


def test_update_view_response_status_code_200_ok(dummy_request):
    """Test if request will return 200 ok response."""
    response = update_view(dummy_request)
    assert response.status_code == 200


def test_list_view_response_text_has_proper_content_type(dummy_request):
    """Test that list view returns expected content."""
    response = list_view(dummy_request)
    assert response.content_type == 'text/html'


def test_list_view_response_text_has_proper_content(dummy_request):
    """Test that list view returns expected content."""
    response = list_view(dummy_request)
    text = '<div class="time-stamp">author, date and time created</div>'
    assert text in response.ubody


def test_detail_view_response_text_has_proper_content_type(dummy_request):
    """Test that list view returns expected content."""
    response = detail_view(dummy_request)
    assert response.content_type == 'text/html'


def test_detail_view_response_text_has_proper_content(dummy_request):
    """Test that list view returns expected content."""
    response = detail_view(dummy_request)
    text = '<div class="time-stamp">date time author</div>'
    assert text in response.ubody


def test_create_view_response_text_has_proper_content_type(dummy_request):
    """Test that list view returns expected content."""
    response = create_view(dummy_request)
    assert response.content_type == 'text/html'


def test_create_view_response_text_has_proper_content(dummy_request):
    """Test that list view returns expected content."""
    response = create_view(dummy_request)
    text = '<button type="button" name="submit">Submit</button>'
    assert text in response.ubody
