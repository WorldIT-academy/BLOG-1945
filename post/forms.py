from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length= 50, required=True)
    content = forms.CharField(widget= forms.Textarea, required=True)
    image = forms.ImageField(required= True)