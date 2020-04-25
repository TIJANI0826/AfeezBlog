from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = '__all__'

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass