from django.db import models

# Create your models here.

PRIORITY_CHOICES = (
        ('high','High'),
        ('med', 'Medium'),
        ('low', 'Low'),
        )

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    completed_time = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES, default='med', null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return self.title
