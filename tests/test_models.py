#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-history
------------

Tests for `django-history` models module.
"""
from django.test import TestCase

from django_history.models import ModelRegistry
from tests.fake_models.models import FakeReference, FakeModel

class TestDjangoHistory(TestCase):

    def setUp(self):
        self.fake_ref = FakeReference.objects.create()
        self.fake_model = FakeModel.objects.create(charfield=":)",
                                              floatfield=20.3,
                                              fkfield=self.fake_ref)

    def test_change_charfield(self):
        self.fake_model.charfield = "Changed"
        self.fake_model.save()
        mr = ModelRegistry.objects.last()
        self.assertEqual(ModelRegistry.objects.count(), 1)
        self.assertEqual(mr.diff, {"charfield": [":)", "Changed"]})
        self.fake_model = mr.rollback_change()
        self.assertEqual(self.fake_model.charfield, ":)")

    def test_change_floatfile(self):
        self.fake_model.floatfield = 19.8
        self.fake_model.save()
        mr = ModelRegistry.objects.last()
        self.assertEqual(ModelRegistry.objects.count(), 1)
        self.assertEqual(mr.diff, {"floatfield": [20.3, 19.8]})
        self.fake_model = mr.rollback_change()
        self.assertEqual(self.fake_model.floatfield, 20.3)


    def test_change_fkfield(self):
        fake_ref2 = FakeReference.objects.create()
        self.fake_model.fkfield = fake_ref2
        self.fake_model.save()
        mr = ModelRegistry.objects.last()
        self.assertEqual(ModelRegistry.objects.count(), 1)
        self.assertEqual(mr.diff, {"fkfield": [self.fake_ref.id, fake_ref2.id]})
        self.fake_model = mr.rollback_change()
        self.assertEqual(self.fake_model.fkfield, self.fake_ref)

    def test_rollback_deleted_obj(self):
        fake_ref2 = FakeReference.objects.create()
        self.fake_model.fkfield = fake_ref2
        self.fake_model.save()
        FakeModel.objects.filter(id=self.fake_model.id).delete()
        mr = ModelRegistry.objects.last()
        self.assertEqual(ModelRegistry.objects.count(), 1)
        self.assertEqual(mr.diff, {"fkfield": [self.fake_ref.id, fake_ref2.id]})
        with self.assertRaises(FakeModel.DoesNotExist) as e:
            mr.rollback_change()
        self.assertEqual(str(e.exception), "FakeModel matching query does not exist.")