from django.db import models

# Create your models here.
from django.db.models import CharField, BooleanField


class TodoItem(models.Model):
    description = CharField(max_length=120, default="", null=False, blank=False)
    done = BooleanField(default=False, null=False)

    def __str__(self):
        base = self.description
        if self.done:
            base = base + "[done]"
        return base