from django import forms
from .models import Hospital
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class DateInput(forms.DateInput):
    input_type = 'date'


class HospitalRegistration(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'admin_name', 'region', 'admin_email', 'admin_phone',
                  'date_from', 'date_due']
        widgets = {
            "date_from": DateInput(),
            "date_due": DateInput(),
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout()

        for field in self.Meta().fields:
            helper.layout.append(field)

        return helper
