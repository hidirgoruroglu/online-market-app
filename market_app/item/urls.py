from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import detail_view,add_item_view,delete_item_view,edit_item_view,items

app_name = "item"

urlpatterns = [
    path("",items,name="items"),
    path("item/<int:id>/",detail_view,name="detail_view"),
    path("add-new-item/",add_item_view,name="add_item_view"),
    path("delete-item/<int:id>/",delete_item_view,name="delete_item_view"),
    path("edit-item/<int:id>/",edit_item_view,name="edit_item_view"),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
