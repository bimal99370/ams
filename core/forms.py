from django import forms
from .models import *

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'name', 'image', 'email', 'primary_contact_number', 'secondary_contact_number',
            'date_of_birth', 'pincode', 'address', 'nationality', 'gender', 'state', 'district',
            'role', 'batting_style', 'bowling_style', 'handedness', 'aadhar_number', 'sports_role',
            'id_card_number', 'weight', 'height', 'age_category', 'team', 'position', 'medical_certificates',
            'aadhar_card_upload', 'pan_card_upload', 'marksheets_upload', 'guardian_name', 'relation',
            'guardian_mobile_number', 'disease', 'allergies', 'additional_information', 'groups'

        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'primary_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'secondary_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'batting_style': forms.TextInput(attrs={'class': 'form-control'}),
            'bowling_style': forms.TextInput(attrs={'class': 'form-control'}),
            'handedness': forms.Select(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
            'sports_role': forms.TextInput(attrs={'class': 'form-control'}),
            'id_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'age_category': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_certificates': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'aadhar_card_upload': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pan_card_upload': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'marksheets_upload': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control'}),
            'relation': forms.Select(attrs={'class': 'form-control'}),
            'guardian_mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'disease': forms.TextInput(attrs={'class': 'form-control'}),
            'allergies': forms.TextInput(attrs={'class': 'form-control'}),
            'additional_information': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

            'groups': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['image'].required = True
        self.fields['email'].required = True
        self.fields['primary_contact_number'].required = True
        self.fields['date_of_birth'].required = True
        self.fields['pincode'].required = True
        self.fields['address'].required = False
        self.fields['nationality'].required = False
        self.fields['gender'].required = False
        self.fields['state'].required = False
        self.fields['district'].required = False
        self.fields['role'].required = False
        self.fields['batting_style'].required = False
        self.fields['bowling_style'].required = False
        self.fields['handedness'].required = False
        self.fields['aadhar_number'].required = True
        self.fields['sports_role'].required = False
        self.fields['id_card_number'].required = False
        self.fields['weight'].required = False
        self.fields['height'].required = False
        self.fields['age_category'].required = False
        self.fields['team'].required = False
        self.fields['position'].required = False
        self.fields['medical_certificates'].required = False
        self.fields['aadhar_card_upload'].required = True
        self.fields['pan_card_upload'].required = False
        self.fields['marksheets_upload'].required = False
        self.fields['guardian_name'].required = False
        self.fields['relation'].required = False
        self.fields['guardian_mobile_number'].required = False
        self.fields['disease'].required = False
        self.fields['allergies'].required = False
        self.fields['additional_information'].required = False

    def clean_primary_contact_number(self):
        data = self.cleaned_data.get('primary_contact_number')
        if data and not data.isdigit():
            raise forms.ValidationError("Primary contact number must contain only digits.")
        return data

    def clean_secondary_contact_number(self):
        data = self.cleaned_data.get('secondary_contact_number')
        if data and not data.isdigit():
            raise forms.ValidationError("Secondary contact number must contain only digits.")
        return data

    def clean_aadhar_number(self):
        data = self.cleaned_data.get('aadhar_number')
        if data and (not data.isdigit() or len(data) != 12):
            raise forms.ValidationError("Aadhar number must be 12 digits.")
        return data

    def clean_pincode(self):
        data = self.cleaned_data.get('pincode')
        if data and (not data.isdigit() or len(data) != 6):
            raise forms.ValidationError("Pincode must be 6 digits, Pincode must be numbers")
        return data

    def clean_state(self):
        data = self.cleaned_data.get('state')
        valid_states = [state[0] for state in Player.STATES]
        if data not in valid_states:
            raise forms.ValidationError("Invalid state selected.")
        return data

    def clean_district(self):
        data = self.cleaned_data.get('district')
        if data and (not data.isalpha() or len(data) < 3):
            raise forms.ValidationError("District must contain only letters and be at least 3 characters long.")
        return data


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']