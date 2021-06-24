from django import forms
from django import forms
listtypes=("home","work","casual","education","medical")
class CreateList(forms.Form):

    name=forms.CharField(label='Name', max_length=200)

    #list_type=forms.ChoiceField(choices=listtypes,label='List Type')


    


