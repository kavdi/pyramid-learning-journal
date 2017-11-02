"""."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound
from blog_post import POSTS

FMT = '%Y/%m/%d'


@view_config(route_name='home', renderer="learning_journal:templates/home_page.jinja2")
def list_view(request):
    return {
        "Title": "Blogs",
        "posts": POSTS
    }


@view_config(route_name='detail', renderer="learning_journal:templates/view_entry.jinja2")
def detail_view(request):
    post_id = int(request.matchdict['id'])
    if post_id < 0 or post_id > len(POSTS) - 1:
        raise HTTPNotFound
    posts = list(filter(lambda posts: posts['id'] == post_id, POSTS))[0]
    return {
        'title': 'Blog Post',
        'posts': POSTS
    }


@view_config(route_name="create", renderer="learning_journal:templates/crea_entry.jinja2")
def create_view(request):
    post_id = list(filter(lambda post: post['id'] == post_id, POSTS))[0]
    return {
        'title': 'Create Blog Post',
    }


@view_config(route_name="update", renderer="learning_journal:templates/edit_entry.jinja2")
def update_view(request):
    post_id = int(request.matchdict['id'])
    if post_id < 0 or post_id > len(POSTS) - 1:
        raise HTTPNotFound
    posts = list(filter(lambda post: post['id'] == post_id, POSTS))[0]
    return {
        'title': 'Edit Post',
        'posts': POSTS
    }
