from django import forms
from . import models

class LoginForm(forms.Form):
  email=forms.EmailField(widget=forms.EmailInput({'placeholder': 'Email'}))
  password=forms.CharField(widget=forms.PasswordInput({'placeholder':'Password'}))

  def clean(self):
    email=self.cleaned_data.get('email')
    password=self.cleaned_data.get('password')

    try:
      user=models.User.objects.get(email=email)
      if user.check_password(password):
        return self.cleaned_data
      else:
        self.add_error('password', forms.ValidationError('password is wrong'))

    except models.User.DoesNotExist:
      self.add_error('email', forms.ValidationError('User does not exist'))

  # class Meta:
  #       model = models.User
  #   fields = ['Email','Password']

class SignUpform(forms.ModelForm):
  class Meta:
    model=models.User
    fields=('email','password','name','student_num','grade','phone_num','first_major','second_major')
    widgets={
      'email':forms.EmailInput(attrs={'class': "form-control-input", 'placeholder':'Email'}),
      'password':forms.PasswordInput(attrs={'class': "form-control-input", 'placeholder':'Password'}),
      'name':forms.TextInput(attrs={'class': "form-control-input", 'placeholder':'name'}),
      'student_num':forms.TextInput(attrs={'class': "form-control-input", 'placeholder':'student_num'}),
      'grade':forms.TextInput(attrs={'class': "form-control-input", 'placeholder':'grade'}),
      'phone_num':forms.TextInput(attrs={'class': "form-control-input", 'placeholder':'phone_num'}),
      'first_major':forms.TextInput(attrs={'class': "form-control-input", 'placeholder':'first_major'}),
      'second_major':forms.TextInput(attrs={'class': "form-control-input", 'placeholder':'second_major'}),
    }

    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

  def clean_email(self):
    email=self.cleaned_data.get('email')
    try:
      models.User.objects.get(email=email)
      raise forms.ValidationError(
        'this email is already exist'
      )
    except models.User.DoesNotExist:
      return email

  def clean_password(self):
        password=self.cleaned_data.get('password')
        return password

  def save(self, *args, **kwargs):
        user=super().save(commit=False)
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        user.username=email
        user.set_password(password)
        user.save()