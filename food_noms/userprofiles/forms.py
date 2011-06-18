from django.db import models
from django import forms
from django.forms import ModelForm
from userprofiles.models import *

class ProfileForm(ModelForm):
     def __init__(self, *args, **kwargs):
          super(ProfileForm, self).__init__(*args, **kwargs)
          try:
               self.fields['email'].initial = self.instance.user.email
               self.fields['first_name'].initial = self.instance.user.first_name
               self.fields['last_name'].initial = self.instance.user.last_name
          except User.DoesNotExist:
               pass

     email = forms.EmailField(label="Email",help_text='')
     first_name = forms.CharField(label="First Name")
     last_name = forms.CharField(label="Last Name")

     class Meta:
          model = UserProfile
          exclude = ('user',)

     def save(self, *args, **kwargs):
          u = self.instance.user
          u.email = self.cleaned_data['email']
          u.first_name = self.cleaned_data['first_name']
          u.last_name = self.cleaned_data['last_name']
          u.save()
          profile = super(ProfileForm, self).save(*args, **kwargs)
          return profile
