from sqlite3 import Row
from tkinter import Widget
from django.db import models
from datetime import date

# Create your views here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    due_date = models.DateField()
    date_stamp = date.today().strftime("%B %d, %Y")
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} due {self.due_date}"