from django.db import models
from datetime import date


class Player(models.Model):
    # Player Information
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    # image = models.ImageField(upload_to='core/static', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    primary_contact_number = models.CharField(max_length=15, blank=True, null=True)
    secondary_contact_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    STATES = [
        ('Karnataka', 'Karnataka'),
        ('Maharashtra', 'Maharashtra'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('others','others')
    ]

    DISTRICTS = {
        'Karnataka': [('Bangalore', 'Bangalore'), ('Mysore', 'Mysore'), ('Hubli', 'Hubli')],
        'Maharashtra': [('Mumbai', 'Mumbai'), ('Pune', 'Pune'), ('Nagpur', 'Nagpur')],
        'Tamil Nadu': [('Chennai', 'Chennai'), ('Coimbatore', 'Coimbatore'), ('Madurai', 'Madurai')],

   }

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None  # or return a default value like 0 if you prefer


    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=10, choices=gender_choices, blank=True, null=True)
    state = models.CharField(max_length=20, choices=STATES, blank=True, null=True)
    district = models.CharField(max_length=100,choices=DISTRICTS, blank=True, null=True)
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
    # medical_certificates = models.FileField(upload_to='core/static', blank=True, null=True)
    medical_certificates = models.FileField(upload_to='certificates/', blank=True, null=True)


    # Parents/Guardian Information
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    relation_choices = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother','Brother'),
        ('Guardian', 'Guardian'),
        ('Other', 'Other')
    ]
    relation = models.CharField(max_length=20, choices=relation_choices, blank=True, null=True)
    guardian_mobile_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
