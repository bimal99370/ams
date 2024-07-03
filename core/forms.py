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
