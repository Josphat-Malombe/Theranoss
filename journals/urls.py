from django.urls import path
from . import views

app_name='journals'
urlpatterns=[
    
    path('' ,views.JournalEntryListView.as_view(), name="entry_list"),
    path('entry/<int:pk>/' ,views.JournalEntryDetailView.as_view(), name="entry_detail "),
    path('create/' ,views.JournalEntryCreateView.as_view(), name="entry_create"),
    path('entry/<int:pk>/update/' ,views.JournalEntryUpdateView.as_view(), name="entry_update"),
    path('entry/<int:pk>/delete/' ,views.JournalEntryDetailView.as_view(), name="entry_delete"),
]