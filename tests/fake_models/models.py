from django.db import models

from django_history.mixins import ModelDiffMixin


class FakeReference(models.Model):
    name = models.CharField(max_length=7, default="FakeRef")


class FakeModel(ModelDiffMixin, models.Model):
    charfield = models.CharField(max_length=30, default='')
    floatfield = models.FloatField(default=0)
    fkfield = models.ForeignKey(FakeReference, on_delete=models.CASCADE)