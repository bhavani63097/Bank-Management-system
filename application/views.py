from django.shortcuts import render,redirect
from application.models import account,announcement
from application.forms import account_form,announcement_form,deposit_form,withdraw_form,transfor_form
from django.db.models import Sum,Count
from django.utils.timezone import now


def login(request):
  return render(request,'login.html')

def dash(request):
  y=account.objects.aggregate(x=Sum('Current_balance'))
  a=account.objects.aggregate(b=Count('Current_balance'))
  return render(request,'dash.html',{'y':y['x'],'a':a['b']})

def accounts(request):
  query=request.GET.get('query','')
  if query: 
    x=account.objects.filter(First_name=query)
  else:
    x=account.objects.all()
  return render(request,'account.html',{'x':x,'query':query}) 

def add_account(request):
  form=account_form()
  if request.method=="POST":
    form=account_form(request.POST)
    if form.is_valid():
      form.save()
  return render(request,'account.html',{'form':form})
    
def up_account(request,id):
  a=account.objects.get(id=id)
  if request.method=="POST":
    y=account_form(request.POST, instance=a)
    if y.is_valid():
      y.save()
  else:
      y=account_form(instance=a)
  return render(request,'account.html',{'y':y})
  
def del_account(request,id):
  a=account.objects.get(id=id)
  a.delete()
  return render(request,'account.html')


def announcements(request):
  query=request.GET.get('query','')
  if query:
    x=announcement.objects.filter(Title=query)
  else:
    x=announcement.objects.all()
  return render(request,'announcement.html',{'x':x,'query':query})

def add_announcement(request):
  form=announcement_form()
  if request.method=="POST":
    form=announcement_form(request.POST)
    if form.is_valid():
      form.save()
  return render(request,'announcement.html',{'form':form})

def up_announcement(request,id):
  a=announcement.objects.get(id=id)
  if request.method=="POST":
    y=announcement_form(request.POST,instance=a)
    if y.is_valid():
      y.save()
  else:
    y=announcement_form(instance=a)
  return render(request,'announcement.html',{'y':y})

def del_announcement(request,id):
  a=announcement.objects.get(id=id)
  a.delete()
  return render(request,'announcement.html')


def tran_admin(request):
  
  query=request.GET.get('query','')
  if query:
    x=account.objects.filter(Middle_name=query)
  else:
    x=account.objects.all()
  return render(request,'tran_admin.html',{'x':x,'query':query})


def dep_admin(request):
    query = request.GET.get('query', '')
    query_1 = request.GET.get('query_1', '')
    x = None
    if query:
      x = account.objects.get(Account_number=query)
    if query_1:
      x.Current_balance+=int(query_1)
      x.save()
    return render(request, 'dep_admin.html', {'x': x, 'query': query, 'query_1': query_1})



def with_admin(request):
    query = request.GET.get('query', '')
    query_1 = request.GET.get('query_1', '')
    x = None
    if query:
      x = account.objects.get(Account_number=query)
    if query_1:
      x.Current_balance-=int(query_1)
      x.save()
    return render(request, 'with_admin.html', {'x': x, 'query': query, 'query_1': query_1})


def tran_from_admin(request):
  
    query = request.GET.get('query', '')
    query_1 = request.GET.get('query_1', '')
    query_2 = request.GET.get('query_2', '')
    x = None
    y = None
    if query:
      x = account.objects.get(Account_number=query)
    if query_1:
      x.Current_balance-=int(query_1)
      x.save()
    if query_2:
      y = account.objects.get(Account_number=query_2)
      y.Current_balance +=int(query_2)
      y.save()
    return render(request, 'tran_from_admin.html', {'x': x, 'query': query, 'query_1': query_1,'y':y,'query_2':query_2})

def login_user(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        filtered_data = account.objects.filter(Email=email, Password=password)
        if filtered_data.exists():
            request.session['filtered_data_Account_number'] = list(
                filtered_data.values_list('Account_number', flat=True)
            )
            return redirect('home')
        else:
            error = 'Invalid email or password. Please try again.'
    return render(request, 'login_user.html', {'error': error})


def home(request):
    filtered_data_Account_number = request.session.get('filtered_data_Account_number', [])
    if not filtered_data_Account_number:
        return redirect('login_user')
    x = account.objects.filter(Account_number__in=filtered_data_Account_number)
    return render(request, 'home.html', {'x': x})


def tran_user(request):
    filtered_data_Account_number = request.session.get('filtered_data_Account_number', [])
    if not filtered_data_Account_number:
        return redirect('login_user')
    a = filtered_data_Account_number[0]
    x = account.objects.filter(Account_number__in=filtered_data_Account_number)
    y = account.objects.get(Account_number=a)
    return render(request, 'tran_user.html', {'x': x, 'y': y})


def dep_user(request):
    filtered_data_Account_number = request.session.get('filtered_data_Account_number', [])
    if not filtered_data_Account_number:
        return redirect('login_user')
    a = filtered_data_Account_number[0]
    obj = account.objects.get(Account_number=a)
    x = deposit_form(initial={'Account_number': a})
    if request.method == 'POST':
        x = deposit_form(request.POST)
        if x.is_valid():
            deposit = x.save(commit=False)
            obj.Deposit_amount = deposit.Deposit_amount
            obj.Current_balance += obj.Deposit_amount
            obj.Dep_date = now()
            obj.save()
            return redirect('home')
    return render(request, 'dep_user.html', {'x': x, 'obj': obj})


def with_user(request):
    filtered_data_Account_number = request.session.get('filtered_data_Account_number', [])
    if not filtered_data_Account_number:
        return redirect('login_user')
    a = filtered_data_Account_number[0]
    obj = account.objects.get(Account_number=a)
    x = withdraw_form(initial={'Account_number': a})
    if request.method == 'POST':
        x = withdraw_form(request.POST)
        if x.is_valid():
            form = x.save(commit=False)
            obj.Withdraw_amount = form.Withdraw_amount
            if obj.Withdraw_amount > obj.Current_balance:
                x.add_error(None, 'Insufficient balance for this withdrawal.')
            else:
                obj.Current_balance -= obj.Withdraw_amount
                obj.With_date = now()
                obj.save()
                return redirect('home')
    return render(request, 'with_user.html', {'x': x, 'obj': obj})


def tran_from_user(request):
    filtered_data_Account_number = request.session.get('filtered_data_Account_number', [])
    if not filtered_data_Account_number:
        return redirect('login_user')
    a = filtered_data_Account_number[0]
    obj = account.objects.get(Account_number=a)
    x = transfor_form(initial={'Account_number': a})
    error = None
    if request.method == 'POST':
        x = transfor_form(request.POST)
        if x.is_valid():
            form = x.save(commit=False)
            transfor = request.POST.get('transfor', '').strip()
            try:
                to = account.objects.get(Account_number=transfor)
                obj.Transfor_amount_from = form.Transfor_amount_from
                if obj.Transfor_amount_from > obj.Current_balance:
                    error = 'Insufficient balance for this transfer.'
                elif to.Account_number == obj.Account_number:
                    error = 'Cannot transfer to the same account.'
                else:
                    obj.Current_balance -= obj.Transfor_amount_from
                    to.Current_balance += obj.Transfor_amount_from
                    to.save()
                    obj.save()
                    return redirect('home')
            except account.DoesNotExist:
                error = f'Account "{transfor}" not found.'
    return render(request, 'tran_from_user.html', {'x': x, 'obj': obj, 'error': error})

