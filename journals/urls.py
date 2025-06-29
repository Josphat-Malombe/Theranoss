# your_journal_app_name/urls.py

from django.urls import path
from .views import (
    JournalEntryListView,
    JournalEntryDetailView,
    JournalEntryCreateView,
    JournalEntryUpdateView,
    JournalEntryDeleteView
)

urlpatterns = [
  
    path('', JournalEntryListView.as_view(), name='journal_list'),
    path('create/', JournalEntryCreateView.as_view(), name='entry_create'),
    path('<int:pk>/', JournalEntryDetailView.as_view(), name='entry_detail'),
    path('<int:pk>/edit/', JournalEntryUpdateView.as_view(), name='entry_update'),
    path('<int:pk>/delete/', JournalEntryDeleteView.as_view(), name='entry_delete'),
]
