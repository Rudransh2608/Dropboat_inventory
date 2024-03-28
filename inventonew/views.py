from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import Usermodifyform, profileupdateform
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required
from project.models import Project
from django.contrib.auth.models import User
from order.models import Order
from product.models import Product


def logout_user(request):
    logout(request)
    return redirect('/login/')

@login_required
def index(request):
   staffw=User.objects.all()
   product=Product.objects.all()
   order=Order.objects.all()
   project=Project.objects.all()
   order_count=order.count()
   product_count=product.count()
   project_count=project.count()
   staff_count=staffw.count()
   context={
      'staffw':staffw,
      'project':project,
      'order':order,
      'order_count':order_count,
      'product':product,
      'product_count': product_count,
      'project_count':project_count,
      'staff_count':staff_count
   }
   if request.method=='POST':
      name=request.POST.get('num5')
      price=request.POST.get('num6')
      enny=Order(oname=name,oprice=price)
      enny.save()
   return render(request,"index.html",context)


def register(request):
    if request.method == 'POST':
     form=Usermodifyform(request.POST)
     if form.is_valid():
        form.save()
        return redirect('/')
    else:
       form=Usermodifyform()
    context={
        'form':form
    }
    return render(request,'register.html',context)

@login_required
def project(request):
   project=Project.objects.all()
   context={
      'project':project
   }
   if request.method=='POST':
      namea=request.POST.get('num')
      qua=request.POST.get('num2')
      cname=request.POST.get('num3')
      enn=Project(name=namea,quantity=qua,clname=cname)
      enn.save()
   return render(request,"project.html",context)

@login_required
def deleteproject(request,id):
   dele= Project.objects.get(id=id)
   dele.delete()
   return redirect('/projects/')

@login_required
def staffo(request):
   staffw=User.objects.all()
   context ={
      'staffw':staffw
   }
   return render(request,'staff.html',context)

@login_required
def orderon(request):
   order=Order.objects.all()
   order_count=order.count()
   context={
      'order':order,
      'order_count':order_count
   }
   if request.method=='POST':
      name=request.POST.get('num5')
      price=request.POST.get('num6')
      enny=Order(oname=name,oprice=price)
      enny.save()
   return render(request,"staffonly.html",context)

@login_required
def profile(request):
   return render(request,'profile.html')

@login_required
def profile_update(request):
   if request.method == 'POST':
     profile_form = profileupdateform(request.POST, instance=request.user.profile)
     if profile_form.is_valid():
        profile_form.save()
        return redirect('/profile_user/')
   else:
     profile_form = profileupdateform(instance=request.user.profile)
   context={
   'profile_form':profile_form
   }
   return render(request,'profileupdate.html',context)

@login_required
def orders(request):
   order=Order.objects.all()
   context={
      'order':order
   }
   if request.method=='POST':
      name=request.POST.get('num5')
      price=request.POST.get('num6')
      enny=Order(oname=name,oprice=price)
      enny.save()
   return render(request,'orders.html',context)

@login_required
def deleteorder(request,id):
   dele= Order.objects.get(id=id)
   dele.delete()
   return redirect('/orders/')

@login_required
def products(request):
   product=Product.objects.all()
   context={
      'product':product
   }
   if request.method=='POST':
      name=request.POST.get('numv5')
      price=request.POST.get('numv6')
      enny=Product(pname=name,pquantity=price)
      enny.save()
   return render(request,"product.html",context)

@login_required
def deleteproduct(request,id):
   dele= Product.objects.get(id=id)
   dele.delete()
   return redirect('/products/')

@login_required
def about(request):
   return render(request,'about.html')

@login_required
def help(request):
   return render(request,'help.html')

def home(request):
   return render(request,'home.html')


