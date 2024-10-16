from django import forms
from .models import Post


class ProfileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    bio = forms.CharField(widget=forms.Textarea)
    is_employed = forms.BooleanField()
    STATUS =(
        ('Single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced',)
    )
    marital_status = forms.ChoiceField(choices=STATUS)
    profile_picture = forms.ImageField(required=False)


class UpdateProfileForm(ProfileForm):
    username = forms.CharField()


class PostForm(forms.ModelForm):
    new_hashtags = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('author', 'title', 'content',  'hashtags')