from django import forms
from django.forms import fields
from .models import Facility, Client
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class FacilityCreateForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['KMFL_code', 'facility_name', 'facility_county', 'facility_subcounty', 'facility_type',
                  'facility_owner']

        # Custom form validation

    def clean_item_name(self):
        KMFL_code = self.cleaned_data.get('KMFL_code')
        if not KMFL_code:
            raise forms.ValidationError('This field is required')
        for instance in Facility.objects.all():
            if instance.KMFL_code == KMFL_code:
                raise forms.ValidationError(KMFL_code + ' already exists')
        return KMFL_code


class ClientCreateForm(forms.ModelForm):
    # county= forms.MultipleChoiceField(choices=COUNTY_CHOICES.ClientsToTuples(Client.objects.all())),
    # sub_county= forms.MultipleChoiceField(choices=SUB_COUNTY_CHOICES)
    # gender= forms.MultipleChoiceField(choices=SEX_CHOICES)
    class Meta:
        model = Client
        fields = ['client_name', 'gender', 'DOB', 'phone_no', 'county', 'sub_county']
        widgets = {
            'DOB': DatePickerInput(),
        }

        # Custom form validation

    def clean_item_name(self):
        client_name = self.cleaned_data.get('client_name')
        if not client_name:
            raise forms.ValidationError('This field is required')
        for instance in Client.objects.all():
            if instance.item_name == client_name:
                raise forms.ValidationError(client_name + ' already exists')
        return client_name


class FacilitySearchForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['KMFL_code', 'facility_name']


class PatientSearchForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['id', 'client_name']


class StockIssuedSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField()

    class Meta:
        model = Facility
        fields = ['facility_name']


class ReportSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField()

    class Meta:
        model = Facility
        fields = ['KMFL_code', 'facility_name']


class FacilityUpdateForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['KMFL_code', 'facility_name', 'facility_county', 'facility_subcounty', 'facility_type',
                  'facility_owner']


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'gender', 'DOB', 'phone_no', 'county', 'sub_county']
        widgets = {
            'DOB': DatePickerInput(),
        }


