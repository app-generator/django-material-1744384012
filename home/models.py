# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Patient(models.Model):

    #__Patient_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateTimeField(blank=True, null=True, default=timezone.now)
    gender = models.BooleanField()
    address = models.TextField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    medical_history_summary = models.TextField(max_length=255, null=True, blank=True)
    dental_history_summary = models.TextField(max_length=255, null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=255, null=True, blank=True)
    registration_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Patient_FIELDS__END

    class Meta:
        verbose_name        = _("Patient")
        verbose_name_plural = _("Patient")



#__MODELS__END
