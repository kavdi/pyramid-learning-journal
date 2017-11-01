"""."""
from pyramid.response import Response
import io
import os

HERE = os.path.dirname(__file__)


def list_view(request):
    """."""
    path = os.path.join(HERE, '../templates/home_page.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())


def detail_view(request):
    """."""
    path = os.path.join(HERE, '../templates/view_entry.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())


def create_view(request):
    """."""
    path = os.path.join(HERE, '../templates/crea_entry.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())


def update_view(request):
    """."""
    path = os.path.join(HERE, '../templates/edit_entry.html')
    with io.open(path) as imported_text:
        return Response(imported_text.read())
