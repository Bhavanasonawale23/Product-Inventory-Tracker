from django.shortcuts import render,redirect
from .models import Product
#(.models => productapp.models) no need to write package_name if you are in/working in same package


# Create your views here.
def home_view(request):
    #db =Product.objects.all()
    #context={'products':db}
    return render(request,'productapp/home.html')

def insert_view(request):
    print(request.method)

    if request.method == "POST":
        print(request.POST)

        pname=request.POST.get('pn')
        pprice=int(request.POST.get('pp'))
        pqty=int(request.POST.get('pq'))
        cat=request.POST.get('pc')

        if (pqty < 0 or pprice <= 0):
            context = {"msg2":"Invalid input. Please enter Positive values."}
            return render(request,"productapp/insert.html",context)

        obj=Product(pname=pname,price=pprice,qty=pqty,category=cat)
        obj.save()
        context={'msg':"Product inserted successfully in DB."}
        return render(request,'productapp/insert.html',context)

    return render(request,'productapp/insert.html')

def display_view(request):
    db=Product.objects.all()
    context={'products':db}
    return render(request,'productapp/display.html',context)

def edit_view(request,pid):

    obj =Product.objects.get(p_id=pid)
    if request.method =='POST':
        upn =request.POST.get('pn')
        upp=int(request.POST.get('pp'))
        upq=int(request.POST.get('pq'))     
        ucat=request.POST.get('pc')

        obj.pname=upn
        obj.price=upp   
        obj.qty=upq
        obj.category=ucat  

        obj.save()
        
        return redirect('display')
    
    context={'product':obj}
    return render(request,'productapp/edit.html',context)

def delete_view(request,pid):
    obj=Product.objects.get(p_id=pid)
    if request.method=='POST':
        obj.delete()
        return redirect('display')  
        

    context = {'product': obj}
    return render(request, 'productapp/delete.html', context)
    
    

    

   