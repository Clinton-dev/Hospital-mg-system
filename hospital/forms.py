from django import forms
from .models import Hospital
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


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
        helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                Column('admin_name', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('region', css_class='form-group col-md-6'),
                Column('admin_email', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('admin_phone', css_class='form-group col-md-6'),
                Column('date_from', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('date_due', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Create new hospital Instance',
                   css_class='btn btn-primary')
        )
        return helper
