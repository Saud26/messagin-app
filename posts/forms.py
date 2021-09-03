from django import forms

from .models import Post

class SubmitPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user', 'published_date']

    
    def __init__(self, *args, **kwargs):
        super(SubmitPostForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs = {'class': 'input', 'placeholder': 'Title'}
        self.fields['description'].widget.attrs = {'class': 'input des', 'placeholder': 'Text (optional)'}