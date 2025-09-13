from django import forms
from django.contrib.auth.models import User
from .models import Treinador

class UserRegistrationForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput)

   class Meta:
      model = User
      fields = ('username', 'password')

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.label_suffix = ""
      self.fields['username'].help_text = None

   def save(self, commit=True):
      user = super().save(commit=False)
      user.set_password(self.cleaned_data["password"])
      if commit:
         user.save()
         Treinador.objects.create(user=user)
      return user

class UserLoginForm(forms.Form):
   username = forms.ChoiceField(label="Username")
   password = forms.CharField(widget=forms.PasswordInput)

   def __init__(self, *args, **kwargs):
      choices = kwargs.pop('choices', [])
      super().__init__(*args, **kwargs)
      self.label_suffix = ""
      self.fields['username'].choices = choices