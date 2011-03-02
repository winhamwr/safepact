from django import forms

class ContractorSignupForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    primary_contact_first_name = forms.CharField(max_length=100)
    primary_contact_last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    confirm_email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    how_did_you_hear_about_us = forms.ChoiceField(choices=(('A', 'AAA'),('B', 'BBB'),('C','CCC')))
    
class HomeownerSignupForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    confirm_email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    how_did_you_hear_about_us = forms.ChoiceField(choices=(('A', 'AAA'),('B', 'BBB'),('C','CCC')))
