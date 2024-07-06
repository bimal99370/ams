from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'name', 'image', 'email', 'primary_contact_number', 'secondary_contact_number',
            'date_of_birth', 'gender', 'state', 'district', 'pincode', 'address', 'role',
            'batting_style', 'bowling_style', 'handedness', 'aadhar_number', 'sports_role',
            'id_card_number', 'medical_certificates', 'guardian_name', 'relation', 'guardian_mobile_number'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'primary_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'secondary_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'batting_style': forms.TextInput(attrs={'class': 'form-control'}),
            'bowling_style': forms.TextInput(attrs={'class': 'form-control'}),
            'handedness': forms.Select(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
            'sports_role': forms.TextInput(attrs={'class': 'form-control'}),
            'id_card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'medical_certificates': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'guardian_name': forms.TextInput(attrs={'class': 'form-control'}),
            'relation': forms.Select(attrs={'class': 'form-control'}),
            'guardian_mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

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
            raise forms.ValidationError("Pincode must be 6 digits.")
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
