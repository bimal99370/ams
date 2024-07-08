from django.db import models
from datetime import date


class Player(models.Model):
    # Player Information
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    email = models.EmailField(blank=True, null=True)
    primary_contact_number = models.CharField(max_length=15, blank=True, null=True)
    secondary_contact_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    STATES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Delhi', 'Delhi'),
        ('Puducherry', 'Puducherry'),
        ('Ladakh', 'Ladakh'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('others', 'others')
    ]

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None

    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True, null=True)
    state = models.CharField(max_length=40, choices=STATES, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)

    # Sports Related
    batting_style = models.CharField(max_length=100, blank=True, null=True)
    bowling_style = models.CharField(max_length=100, blank=True, null=True)
    handedness_choices = [('R', 'Right'), ('L', 'Left')]
    handedness = models.CharField(max_length=1, choices=handedness_choices, blank=True, null=True)
    aadhar_number = models.CharField(max_length=12, blank=True, null=True)
    sports_role = models.CharField(max_length=100, blank=True, null=True)
    id_card_number = models.CharField(max_length=50, blank=True, null=True)

    # Files/Documents Section
    medical_certificates = models.FileField(upload_to='certificates/', blank=True, null=True)
    aadhar_card_upload = models.FileField(upload_to='documents/aadhar/', blank=True, null=True)
    pan_card_upload = models.FileField(upload_to='documents/pan/', blank=True, null=True)
    marksheets_upload = models.FileField(upload_to='documents/marksheets/', blank=True, null=True)

    # Parents/Guardian Information
    guardian_name = models.CharField(max_length=100, blank=True, null=True)

    relation_choices = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother', 'Brother'),
        ('Guardian', 'Guardian'),
        ('Other', 'Other')
    ]

    relation = models.CharField(max_length=20, choices=relation_choices, blank=True, null=True)
    guardian_mobile_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
