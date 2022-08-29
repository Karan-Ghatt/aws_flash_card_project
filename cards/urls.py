# cards/urls.py
# both 'cards' directory and urls.py file created manually by user
# then user manually created templates/cards directories and then base.html file in 'cards' directory
from django.urls import path
from . import views

# from django.views.generic import TemplateView
#urlpatterns = [
#    path(
#        "",
#        TemplateView.as_view(template_name="cards/base.html"),
#        name="home"
#    ),
#]


urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card-list"
    ),

    path(
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
    ),

    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),

    path(
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name="box"
    ),

    path(
        "<pk>/delete/",
        views.CardDeleteView.as_view(),
        name="card-delete"
    ),

]

