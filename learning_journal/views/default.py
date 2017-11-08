"""."""
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from learning_journal.models.mymodel import MyModel
from learning_journal.security import security_check
from pyramid.security import remember, forget
from pyramid.security import NO_PERMISSION_REQUIRED

FMT = '%Y/%m/%d'


@view_config(route_name='home', permission='view', renderer="learning_journal:templates/home_page.jinja2")
def list_view(request):
    posts = request.dbsession.query(MyModel).all()
    posts = [item.to_dict() for item in posts]
    return {
        "Title": "Blogs",
        "posts": reversed(posts)
    }


@view_config(route_name='detail', permission='view', renderer="learning_journal:templates/view_entry.jinja2")
def detail_view(request):
    posts_id = int(request.matchdict['id'])
    post = request.dbsession.query(MyModel).get(posts_id)
    if post:
        return {
            'title': 'Edit Post',
            'post': post.to_dict()
        }
    raise HTTPNotFound


@view_config(route_name="create", permission='secret', renderer="learning_journal:templates/crea_entry.jinja2")
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
        'date': datetime.now().strftime('%B %d, %Y')
    }


@view_config(route_name="update", permission='secret', renderer="learning_journal:templates/edit_entry.jinja2")
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


@view_config(route_name="delete", permission='secret')
def delete_post(request):
    posts_id = int(request.matchdict['id'])
    post = request.dbsession.query(MyModel).get(posts_id)
    if not post:
        raise HTTPNotFound
    request.dbsession.delete(post)
    return HTTPFound(request.route_url('home'))


@view_config(route_name="login", renderer="learning_journal:templates/login.jinja2", permission=NO_PERMISSION_REQUIRED)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        import pdb;pdb.set_trace()
        if security_check(username, password):
            headers = remember(request, username)
            return HTTPFound(location=request.route_url('home'), headers=headers)
    return {}


@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(request.route_url('home'), headers=headers)
