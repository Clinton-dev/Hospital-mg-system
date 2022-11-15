from django import forms
from .models import Hospital
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'


class HospitalRegistration(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'email', 'phone', 'logo', 'date_established']
        widgets = {
            "date_established": DateInput(),
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout()

        for field in self.Meta().fields:
            helper.layout.append(field)

        return helper

    # for field in self.Meta().fields:
