from django import forms
from application.models import account,announcement
class account_form(forms.ModelForm):
        class Meta:
            model=account
            fields=("Account_number","First_name","Middle_name","Last_name","Email","Password")
class deposit_form(forms.ModelForm):
    class Meta:
        model=account
        fields=['Account_number','Deposit_amount']
       
class withdraw_form(forms.ModelForm):
    class Meta:
        model=account
        fields=['Account_number','Withdraw_amount']
        

class transfor_form(forms.ModelForm):
    class Meta:
        model=account
        fields=['Account_number','Transfor_amount_from']

        
class announcement_form(forms.ModelForm):
    class Meta:
            model=announcement
            fields=['Title','Announcement']