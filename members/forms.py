from django import forms
from .models import Post

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'password1': forms.Password(attrs={'class': 'form-control'}),
            'password2': forms.Password(attrs={'class': 'form-control'}),
        }
