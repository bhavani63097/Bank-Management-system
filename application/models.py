from django.db import models

class account(models.Model):
    Account_number=models.CharField(max_length=50)
    First_name=models.CharField(max_length=50)
    Middle_name=models.CharField(max_length=50,blank=True)
    Last_name=models.CharField(max_length=50,blank=True)
    Email=models.EmailField(max_length=254)
    Password=models.CharField(max_length=50)
    Pin=models.CharField(max_length=50)
    Current_balance=models.IntegerField(default=0)
    Created_at=models.DateTimeField(auto_now_add=True) 
    Updated_at=models.DateTimeField(auto_now=True)
    Deposit_amount=models.IntegerField(default=0)
    Dep_date=models.DateTimeField(null=True, blank=True)
    Withdraw_amount=models.IntegerField(default=0)
    With_date=models.DateTimeField(null=True, blank=True)
    Transfor_amount_from=models.IntegerField(default=0)
    
    
class announcement(models.Model):
    Title=models.CharField(max_length=50)
    Announcement=models.TextField()
    Date_created=models.DateTimeField(auto_now_add=True)
    Date_updated=models.DateTimeField(auto_now=True)
    
    
