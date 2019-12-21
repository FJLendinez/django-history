from django.db import models, transaction
from django.contrib.postgres import fields
from django.apps import apps


class ModelRegistry(models.Model):
    label = models.CharField(max_length=120, default="")
    object_id = models.PositiveIntegerField()
    diff = fields.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)

    def get_registry_for_model(self, model):
        return self.objects.filter(label=model._meta.label)

    def get_object(self):
        app_label, model_name = self.label.split(".")
        Model = apps.get_model(app_label, model_name)
        return Model.objects.get(pk=self.object_id)

    def rollback_change(self):
        obj = self.get_object()
        for k, v in self.diff.items():
            try:
                setattr(obj, k, v[0])
            except ValueError:
                setattr(obj, k+"_id", v[0])
        with transaction.atomic():
            obj.save()
            ModelRegistry.objects.filter(pk=self.pk).delete()
            return obj