from django import forms
from authapp.models import Person, Album

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(label='Release Date', widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Album
        fields = "__all__"