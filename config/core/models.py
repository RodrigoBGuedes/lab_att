from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from ordered_model.models import OrderedModel
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Box(OrderedModel):
    code_box = models.CharField(
        max_length=24, unique=True,
        validators=[MinLengthValidator(24)],
        verbose_name=_('code'),
    )
    description = models.TextField(max_length=100, verbose_name=_('description'))
    is_empty = models.BooleanField(default=False, verbose_name=_('empty'))

    def __str__(self):
        return self.code_box


class Material(OrderedModel):
    code_material = models.CharField(max_length=50, unique=True, verbose_name=_('code'))
    description = models.TextField(max_length=100, verbose_name=_('description'))

    def __str__(self):
        return self.code_material


class Appointment(OrderedModel):
    box = models.ForeignKey(
        Box, on_delete=models.PROTECT, verbose_name=_('box'))

    material = models.ForeignKey(
        Material, on_delete=models.PROTECT, verbose_name=_('material'))

    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('creator'))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))

    def __str__(self):
        return f'{self.box} - {self.material}'
