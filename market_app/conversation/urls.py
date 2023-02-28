from django.urls import path

from .views import new_conversation,inbox,detail

app_name = "conversation"
urlpatterns = [
    path("", inbox, name="inbox"),
    path("detail/<int:id>", detail, name="detail"),
    path("new-conversation/<int:id>/",new_conversation,name="new_conversation"),
]
