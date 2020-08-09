from django import forms
from .models import Post
from .models import Category

# choices = [('sports','sports')]
choices = Category.objects.all().values_list('category_name', 'category_name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','meta_description','category','author','body',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Tagline'}),
            'meta_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Meta Description'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
