from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from django.urls import reverse_lazy

from .forms import UserEntryJournalForm
from .models import UserEntryJournal
# Create your views here.



# Journal Entry Listing View
class JournalEntryListView(ListView):
    model = UserEntryJournal
    template_name = 'journals/journal_list.html' # Name of your provided template
    context_object_name = 'entry' # This is what your template expects: {% for item in entry %}
    paginate_by = 9 # Number of entries per page (adjust as needed for your layout)
    


# Detail View for a single entry
class JournalEntryDetailView(DetailView):
    model = UserEntryJournal
    template_name = 'journals/journal_detail.html' # You'll need to create this template
    context_object_name = 'entry'

# Create View
class JournalEntryCreateView(CreateView):
    model = UserEntryJournal
    form_class = UserEntryJournalForm
    template_name = 'journals/journal_form.html' # Re-use the form template
    success_url = reverse_lazy('journal_list') # Redirect to the list after creation

# Update View
class JournalEntryUpdateView(UpdateView):
    model = UserEntryJournal
    form_class = UserEntryJournalForm
    template_name = 'journals/journal_form.html' # Re-use the form template
    success_url = reverse_lazy('journal_list') # Redirect to the list after update

# Delete View
class JournalEntryDeleteView(DeleteView):
    model = UserEntryJournal
    template_name = 'journals/journal_confirm_delete.html' # Create a simple confirmation template
    success_url = reverse_lazy('journal_list') # Redirect to the list after deletion






"""
def create_journal_entry(request):
    if request.method == 'POST':
        form = UserEntryJournalForm(request.POST)
        if form.is_valid():
            journal_entry = form.save(commit=False)
            # if you have a user field, assign it here:
            # journal_entry.user = request.user
            journal_entry.save()
            return redirect('journal_detail', pk=journal_entry.pk) # Redirect to detail page
    else:
        form = UserEntryJournalForm()
    return render(request, 'journals/journal_form.html', {'form': form})

def journal_detail(request, pk):
    entry = get_object_or_404(UserEntryJournal, pk=pk)
    return render(request, 'journals/journal_detail.html', {'entry': entry})






class JournalEntryListView(LoginRequiredMixin, ListView):
    login_url='users/login/'
    model=UserEntryJournal
    template_name='index.html'
    context_object_name='entry'
    paginate_by=5

    def get_queryset(self):
        #to ensure users only see their own entries

        return UserEntryJournal.objects.filter(user=self.request.user).order_by('-created_at')


class JournalEntryDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=UserEntryJournal
    template_name='view.html'
    context_object_name='entry'

    def test_func(self):
        #To ensure user can view just their own entry
        entry=self.get_object()
        return self.request.user==entry.user
    
class JournalEntryCreateView(LoginRequiredMixin,CreateView):
    model=UserEntryJournal
    template_name='create.html'
    fields=['title','content','mood']
    success_url=reverse_lazy('entry_list')

    def form_valid(self, form):
        #     setting current logged in user as the author
        
        form.instance.user=self.request.user
        return super().form_valid(form)
    

class JournalEntryUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=UserEntryJournal
    template_name='create.html'
    fields=['title','content','mood'] 

    def get_success_url(self):
        return reverse_lazy(' entry_update'  ,kwargs={'pk': self.object.pk})
    
    def test_func(self):
        #To ensure user can update just their own entry
        entry=self.get_object()
        return self.request.user==entry.user
    
class JournalEntryDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=UserEntryJournal
    template_name='delete.html'
    success_url=reverse_lazy('index.html')
    context_object_name='entry'

    def test_func(self):
        #To ensure user can delete just their own entry
        entry=self.get_object()
        return self.request.user==entry.user
"""

