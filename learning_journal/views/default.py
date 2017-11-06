"""."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.data.blog_post import POSTS

FMT = '%Y/%m/%d'


@view_config(route_name='home', renderer="learning_journal:templates/home_page.jinja2")
def list_view(request):
    return {
        "Title": "Blogs",
        "posts": POSTS
    }


@view_config(route_name='detail', renderer="learning_journal:templates/view_entry.jinja2")
def detail_view(request):
    posts_id = int(request.matchdict['id'])
    if posts_id < 0 or posts_id > len(POSTS):
        raise HTTPNotFound
    post = list(filter(lambda posts: posts['id'] == posts_id, POSTS))[0]
    return {
        'title': 'Blog Post',
        'post': post
    }


@view_config(route_name="create", renderer="learning_journal:templates/crea_entry.jinja2")
def create_view(request):
    return {
        'title': 'Create Blog Post',
        'date': datetime.now()
    }


@view_config(route_name="update", renderer="learning_journal:templates/edit_entry.jinja2")
def update_view(request):
    posts_id = int(request.matchdict['id'])
    if posts_id < 0 or posts_id > len(POSTS):
        raise HTTPNotFound
    post = list(filter(lambda post: post['id'] == posts_id, POSTS))[0]
    return {
        'title': 'Edit Post',
        'post': post
    }
