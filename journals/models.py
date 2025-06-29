from django.db import models
from django.conf import settings

from tinymce.models import HTMLField

# Create your models here.

MOOD_CHOICES = [
    ('happy', '😊 Happy'),
    ('sad', '😢 Sad'),
    ('anxious', '😟 Anxious'),
    ('stressed', '😫 Stressed'),
    ('calm', '😌 Calm'),
    ('excited', '😃 Excited'),
    ('neutral', '😐 Neutral'),
]

class UserEntryJournal(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="journal_entries", null=True)
    title=models.CharField(max_length=200)
    content=HTMLField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    mood=models.CharField(max_length=20, choices=MOOD_CHOICES,blank=True,null=True, help_text="How are you feeling? ")


    def __str__(self):
        return f" {self.title} by {self.user.username} at {self.created_at.strftime('%y-%m-%d')}"
    
 
    class Meta:
        ordering=['-created_at']

