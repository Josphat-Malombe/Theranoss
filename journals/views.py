from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy

from .models import UserEntryJournal

# Create your views here.

class JournalEntryListView(LoginRequiredMixin, ListView):
    model=UserEntryJournal
    template_name='entry_list.html'
    context_object_name='entry'
    paginate_by=5

    def get_queryset(self):
        """to ensure users only see their own entries"""

        return UserEntryJournal.objects.filter(user=self.request.user).order_by('-created_at')
    

class JournalEntryDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=UserEntryJournal
    template_name='entry_detail.html'
    context_object_name='entry'

    def test_func(self):
        """To ensure user can view just their own entry"""
        entry=self.get_object()
        return self.request.user==entry.user
    
class JournalEntryCreateView(LoginRequiredMixin,CreateView):
    model=UserEntryJournal
    template_name='entry_form.html'
    fields=['title','content','mood']
    success_url=reverse_lazy('entry_list')

    def form_valid(self, form):
        """
        setting current logged in user as the author
        """
        form.instance.user=self.request.user
        return super().form_valid(form)
    

class JournalEntryUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=UserEntryJournal
    template_name='entry_form'
    fields=['title','content','mood'] 

    def get_success_url(self):
        return reverse_lazy(' entry_detail'  ,kwargs={'pk': self.object.pk})
    
    def test_func(self):
        """To ensure user can update just their own entry"""
        entry=self.get_object()
        return self.request.user==entry.user
    
class JournalEntryDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=UserEntryJournal
    template_name='entry_delete.html'
    success_url=reverse_lazy('entry_list.html')
    context_object_name='entry'

    def test_func(self):
        """To ensure user can delete just their own entry"""
        entry=self.get_object()
        return self.request.user==entry.user


