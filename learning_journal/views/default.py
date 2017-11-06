"""."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models.mymodel import MyModel

FMT = '%Y/%m/%d'


@view_config(route_name='home', renderer="learning_journal:templates/home_page.jinja2")
def list_view(request):
    posts = request.dbsession.query(MyModel).all()
    posts = [item.to_dict() for item in posts]
    return {
        "Title": "Blogs",
        "posts": reversed(posts)
    }


@view_config(route_name='detail', renderer="learning_journal:templates/view_entry.jinja2")
def detail_view(request):
    posts_id = int(request.matchdict['id'])
    post = request.dbsession.query(MyModel).get(posts_id)
    if post:
        return {
            'title': 'Edit Post',
            'post': post.to_dict()
        }
    raise HTTPNotFound


@view_config(route_name="create", renderer="learning_journal:templates/crea_entry.jinja2")
def create_view(request):
    if request.method == "POST" and request.POST:
        post = request.POST
        new_post = MyModel(
            title=post['title'],
            author=post['author'],
            date=datetime.now(),
            text=post['text']
        )
        request.dbsession.add(new_post)
        return HTTPFound(request.route_url('home'))
    return {
        'title': 'Create Blog Post',
        'date': datetime.now()
    }


@view_config(route_name="update", renderer="learning_journal:templates/edit_entry.jinja2")
def update_view(request):
    posts_id = int(request.matchdict['id'])
    posts = request.dbsession.query(MyModel).get(posts_id)
    if posts:
        if request.method == "POST" and request.POST:
            post = request.POST
            posts.title = post['title'],
            posts.text = post['text']

            request.dbsession.flush()
            return HTTPFound(request.route_url('detail', id=posts.id))
        return {
            'title': 'Edit Post',
            'post': posts.to_dict()
        }
    raise HTTPNotFound


@view_config(route_name='delete')
def delete_post(request):
    posts_id = int(request.matchdict['id'])
    post = request.dbsession.query(MyModel).get(posts_id)
    if not post:
        raise HTTPNotFound
    request.dbsession.delete(post)
    return HTTPFound(request.route_url('home'))
