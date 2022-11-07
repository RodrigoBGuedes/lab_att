from django.core.exceptions import ValidationError

from .models import User, Box, Material, Appointment
from django import forms

from django.utils.translation import gettext_lazy as _


class AppointmentFormScan(forms.ModelForm):
    box = forms.CharField(min_length=24, max_length=24, required=True, label=_('Box Number'))

    material = forms.CharField(max_length=50, required=True, label=_('Material Number'))

    class Meta:
        model = Appointment
        exclude = ['box', 'material']

    def clean_box(self):
        b = self.cleaned_data['box']
        if not Box.objects.filter(code_box=b).exists():
            raise ValidationError(_('The box is invalid'))
        elif Box.objects.filter(code_box=b, is_empty=False):
            raise ValidationError(_('The box {b} is not empty').format(b=b))

        return b

    def clean_material(self):
        m = self.cleaned_data['material']
        if not Material.objects.filter(code_material=m).exists():
            raise ValidationError(_('The material is invalid'))

        return m


class AppointmentFormVoice(forms.ModelForm):
    box = forms.CharField(min_length=4, max_length=4, required=True, label=_('Box Number'))

    material = forms.CharField(max_length=50, required=True, label=_('Material Number'))

    class Meta:
        model = Appointment
        exclude = ['box', 'material']

    def clean_box(self):
        b = self.cleaned_data['box']
