# from django.shortcuts import render
# from application.models import account
# from application.forms import account_form
# def dash(request):
#     return render(request,'dash.html')

# def accounts(request):
#   query=request.GET.get('query','')
#   if query: 
#     x=account.objects.filter(First_name=query)
  
#   return render(request,'account.html',{'x':x,'query':query}) 
# import gc
# x = [1, 2, 3]
# y = x         # reference count = 2

# del x 
# # reference count = 1
# y = None      # reference count = 0 → object is freed
# print(gc.isenabled())  


# class x():
#     def __init__(self):
#         print("Construtoor method")
        
#     def  m1(self):
#         print("instance method")
        
#     @staticmethod
#     def  m2():
#         print("static method")
        
#     @classmethod
#     def m3(cls):
#         print("class method")
        
# obj=x()
# obj.m1() 
# obj.m2()
# obj.m3()
    

    
    
    