from django.urls import path, re_path

from list.views import add, show, toggle_done

app_name = 'todo'

urlpatterns = [
    path('', show, name="show"),
    re_path(r'add/?', add, name="add"),
    re_path(r'toggle/(?P<item_id>[0-9]+)/?', toggle_done, name="toggle")
]