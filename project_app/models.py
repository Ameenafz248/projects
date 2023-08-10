from django.db import models
import datetime
from datetime import date
from django import utils
import uuid

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    link = models.URLField(null=False)
    date_added = models.DateField(auto_now_add=True)
    hits = models.IntegerField(default=0)
    description = models.TextField(blank=True)


    def __str__(self) -> str:
        return self.name

    @property
    def relevance(self):
        curr_date = datetime.datetime.strptime(str(date.today()), "%Y-%m-%d")
        date_added = datetime.datetime.strptime(str(self.date_added), "%Y-%m-%d")
        return self.hits * 60 - (curr_date - date_added).days * 5
