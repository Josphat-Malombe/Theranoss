from django import forms

from .models import UserEntryJournal
from tinymce.widgets import TinyMCE


class UserEntryJournalForm(forms.ModelForm):
    content=forms.CharField(
        widget=TinyMCE(attrs={'cols':80, 'rows':30})
    )

    class Meta:
        model=UserEntryJournal
        fields=['title','content']