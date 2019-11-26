from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateNewView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('create_new/', PageCreateNewView.as_view(), name='wiki-create-new-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
