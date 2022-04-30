from django.urls import path
from .views import deleteNote, getRoutes, getNotes, getNote, createNote, updateNote

urlpatterns = [
    path('', getRoutes),
    
    #get all or single notes endpoints
    path('api/v1/notes/', getNotes),
    path('api/v1/notes/<str:pk>/', getNote),

    # create and update notes
    path('api/v1/note/create/', createNote),
    path('api/v1/notes/<str:pk>/update/', updateNote),
    
    # delete notes
    path('api/v1/notes/<str:pk>/delete/', deleteNote),
]