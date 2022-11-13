from django import forms
from django.forms import ModelForm
from . import models


class BrgyInfoForm(ModelForm):
    class Meta:
        model = models.brgy_info
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'brgy_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Barangay Name'}),
            'brgy_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'brgy_province': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Province'}),
            'brgy_contactNo': forms.TextInput(
                attrs={'class': 'form-control mob_no', 'placeholder': 'Phone Number', 'data_mask': '0000 000 0000'}),
            'brgy_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'brgy_history': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'History'}),
            'brgy_logo': forms.FileInput(attrs={'type': 'file', 'class':'form-control', 'id': 'brgy_logo_input' }),
        }


class BrgyPurok(ModelForm):
    class Meta:
        model = models.purok
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'purok_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purok Name'}),
            'purok_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


class ResidentForm(ModelForm):
    class Meta:
        model = models.Resident
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'res_fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'res_lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'res_mname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'res_extname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ext.'}),
            'res_gender': forms.Select(attrs={'class': 'form-control'}),
            'res_bdate': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Birth Date', 'type': 'date'}),
            'res_place_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place of Birth'}),
            'res_purok': forms.Select(attrs={'class': 'form-control'}),
            'res_address1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'res_contactNo': forms.TextInput(attrs={'class': 'form-control mob_no', 'placeholder': 'Contact Number'}),
            'res_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'res_isVoter': forms.Select(attrs={'class': 'form-control'}),
            'res_civil_status': forms.Select(attrs={'class': 'form-control'}),
            'res_occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation'}),
            'res_nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'res_religion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Religion'}),
            'res_photo': forms.FileInput(attrs={'type': 'file', 'class':'form-control', 'id': 'res_photo_input' }),
        }