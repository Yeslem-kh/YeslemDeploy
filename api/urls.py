from django.urls import path
from .views import NoteList,DeleteNote

urlpatterns=[
    path('notes/',NoteList.as_view(),name='notes'),
    path('notes/delete/<int:id>',DeleteNote.as_view(),name='delete-note'),
    
]