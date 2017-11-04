"""."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.models.mymodel import MyModel

FMT = '%Y/%m/%d'


@view_config(route_name='home', renderer="learning_journal:templates/home_page.jinja2")
def list_view(request):
    posts = request.dbsession.query(MyModel).all()
    return {
        "Title": "Blogs",
        "posts": posts
    }


@view_config(route_name='detail', renderer="learning_journal:templates/view_entry.jinja2")
def detail_view(request):
    posts_id = int(request.matchdict['id'])
    posts = request.dbsession.query(MyModel).get(posts_id)
    if posts:
        return {
            'title': 'Edit Post',
            'post': posts
        }
    raise HTTPNotFound


@view_config(route_name="create", renderer="learning_journal:templates/crea_entry.jinja2")
def create_view(request):
    return {
        'title': 'Create Blog Post',
        'date': datetime.now()
    }


@view_config(route_name="update", renderer="learning_journal:templates/edit_entry.jinja2")
def update_view(request):
    posts_id = int(request.matchdict['id'])
    posts = request.dbsession.query(MyModel).get(posts_id)
    if posts:
        return {
            'title': 'Edit Post',
            'post': posts
        }
    raise HTTPNotFound
