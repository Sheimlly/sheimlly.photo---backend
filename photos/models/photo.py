from django.db import models
from . import category

class Photo:
    name = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(category.Category, on_delete=models.PROTECT)