from django.urls import path
from myapp.views import index, delete_item, edit_item

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
    path('edit/<int:item_id>/', edit_item, name='edit_item'),
]

