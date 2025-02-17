from django.shortcuts import render
from application.models import account
from application.forms import account_form
def dash(request):
    return render(request,'dash.html')

def accounts(request):
  query=request.GET.get('query','')
  if query: 
    x=account.objects.filter(First_name=query)
  
  return render(request,'account.html',{'x':x,'query':query}) 

