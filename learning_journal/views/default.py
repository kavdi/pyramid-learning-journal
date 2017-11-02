"""."""
from pyramid.response import Response
from pyramid.view import view_config
from datetime import datetime
from pyramid.httpexceptions import HTTPNotFound
import io
import os

 
 FMT = '%m/%d/%Y'
 EXPENSES = [
     {'id': 1, 'title': 'Rent', 'amount': 50000, 'due_date': datetime.strptime('11/1/2017', FMT)},
     {'id': 2, 'title': 'Phone Bill', 'amount': 100, 'due_date': datetime.strptime('11/27/2017', FMT)},
     {'id': 3, 'title': 'Food', 'amount': 600, 'due_date': datetime.strptime('11/2/2017', FMT)},
     {'id': 4, 'title': 'Car', 'amount': 270, 'due_date': datetime.strptime('11/25/2017', FMT)},
     {'id': 5, 'title': 'Internet', 'amount': 100, 'due_date': datetime.strptime('11/12/2017', FMT)},
 ]


@view_config(route_name='home', renderer="learning_journal:templates/home_page.jinja2")
def list_view(request):
    return {
        "Title": "title",
        "Created": date
    }


@view_config(route_name='detail', renderer="learning_journal:templates/view_entry.jinja2")
def detail_view(request):
    expense_id = int(request.matchdict['id'])
    if expense_id < 0 or expense_id > len(EXPENSES) - 1:
        raise HTTPNotFound
    expense = list(filter(lambda expense: expense['id'] == expense_id, EXPENSES))[0]
    return {
        'title': 'One Expense',
        'expense': expense
    }


@view_config(route_name="create", renderer="learning_journal:templates/crea_entry.jinja2")
def create_view(request):
    expense_id = int(request.matchdict['id'])
    if expense_id < 0 or expense_id > len(EXPENSES) - 1:
        raise HTTPNotFound
    expense = list(filter(lambda expense: expense['id'] == expense_id, EXPENSES))[0]
    expense['due_date'] = expense['due_date'].strftime(FMT)
    return {
        'title': 'One Expense',
        'expense': expense
    }


@view_config(route_name="update", renderer="learning_journal:templates/edit_entry.jinja2")
def update_view(request):
    expense_id = int(request.matchdict['id'])
    if expense_id < 0 or expense_id > len(EXPENSES) - 1:
        raise HTTPNotFound
    expense = list(filter(lambda expense: expense['id'] == expense_id, EXPENSES))[0]
    expense['due_date'] = expense['due_date'].strftime(FMT)
    return {
        'title': 'One Expense',
        'expense': expense
    }


# HERE = os.path.dirname(__file__)


# def list_view(request):
#     """."""
#     path = os.path.join(HERE, '../templates/home_page.html')
#     with io.open(path) as imported_text:
#         return Response(imported_text.read())

# def detail_view(request):
#     """."""
#     path = os.path.join(HERE, '../templates/view_entry.html')
#     with io.open(path) as imported_text:
#         return Response(imported_text.read())


# def create_view(request):
#     """."""
#     path = os.path.join(HERE, '../templates/crea_entry.html')
#     with io.open(path) as imported_text:
#         return Response(imported_text.read())


# def update_view(request):
#     """."""
#     path = os.path.join(HERE, '../templates/edit_entry.html')
#     with io.open(path) as imported_text:
#         return Response(imported_text.read())
