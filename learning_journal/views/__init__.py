"""."""
from learning_journal.views.default import (
    list_view,
    detail_view,
    create_view,
    update_view,
    delete_post
)


def includeme(config):
    """."""
    config.add_view(list_view, route_name='home')
    config.add_view(detail_view, route_name='detail')
    config.add_view(create_view, route_name='create')
    config.add_view(update_view, route_name='update')
    config.add_view(delete_post, route_name='delete')
