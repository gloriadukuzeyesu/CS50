from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_wiki_entry, name="wiki_entry"), 
    path("search/", views.search, name="search"),
    path('new_page/', views.new_page, name="new_page"),
    path('edit/', views.edit, name="edits"),
    path('save_edits/', views.save_edits, name="save_edits"),
    path('random_page/', views.random_page, name="random_page"),
]
