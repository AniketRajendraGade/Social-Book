from django import forms
from .models import CustomUser,Books
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(forms.ModelForm):
    # gender choice
    gender_choice = [
      ("Male", "Male"),
      ("Female", "Female"),
      ("Other","Other"),
    ]
    
    gender = forms.ChoiceField(
        choices = gender_choice,
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )
    
    
    
    
    class Meta:
        model = CustomUser
        fields = ['email', 'user_name', 'full_name', 'gender','public_visibility','birth_year', 'city', 'state', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'public_visibility':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            
        }
        
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        if len(user_name) < 3:
            raise forms.ValidationError('Username must be at least 3 characters long.')
        return user_name

    def check_pasword(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('password must be at least 8 characters long.')
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
class UploadBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'visibility', 'cost', 'year_publish','image', 'file']