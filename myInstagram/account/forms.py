from django import forms
from .models import *
class UserCreationForm(forms.ModelForm):
    passwd1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    passwd2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'first_name', 'last_name', 'gender', 'dob', 'phone']
    def clean_passwd2(self):
        passwd1 = self.cleaned_data.get("passwd1")
        passwd2 = self.cleaned_data.get("passwd2")
        if passwd1 and passwd2 and passwd1 != passwd2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit = False)
        user.set_password(self.cleaned_data["passwd1"])
        if commit:
            user.save()
        return user
