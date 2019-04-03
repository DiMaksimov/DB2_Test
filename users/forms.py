from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import DB2User


class DB2UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = DB2User
        fields = ('username', 'email', 'birthday', 'country', 'city', )
        birthday = forms.DateField(widget=forms.SelectDateWidget)


class DB2UserChangeForm(UserChangeForm):

    class Meta:
        model = DB2User
        fields = ('username', 'email', 'birthday', 'country', 'city', )
        birthday = forms.DateField(widget=forms.SelectDateWidget)
