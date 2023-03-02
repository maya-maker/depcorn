from django.shortcuts import render,redirect
from backend.forms import RegisterForm,VegetableForm,LoginForm,OrderForm
from backend.models import Register,Vegetable,Cart,Order



def order_place(request,str,str2,str3):
    username = str3
    print(str3)
    q = str
    p = str2
    cart = Cart.objects.filter(username = username)
    product_id= [i[j] for i in cart.values() for j in i.keys() if j=="id"]
    print(product_id)
    if request.method =="POST":
        name = request.POST['name']
        phone_no = request.POST['phone_no']
        pincode = request.POST['pincode']
        state = request.POST['state']
        city =request.POST['city']
        address = request.POST['address']
        quantity = request.POST['quantity']
        amount = request.POST['amount']
        order = Order(product_id=product_id,name=name,phone_no=phone_no,pincode=pincode,state=state,city=city,address=address,quantity=quantity,amount=amount)
        order.save()
        return payment(request,p,q,username)
    context = {'cart':cart,'quantity':q,"price":p,'username':username}
    return render(request,'order.html',context)




def index(request):
    try:
       x = request.session['login']
       vegetable = Vegetable.objects.all()
       context = {'vegetable':vegetable,'username':x}
       return render(request,'index.html',context)
    except:
        vegetable = Vegetable.objects.all()
        context = {'vegetable':vegetable}
        return render(request,'index.html',context)

def register(request):
    form = RegisterForm()
    todo = request.session.set_test_cookie()
    print(todo)
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            phone_no = form.cleaned_data['phone_no']
            pwd = form.cleaned_data['pwd']
            x = Register(username=username,phone_no=phone_no,pwd=pwd)
            x.save()
            return redirect('/')
    context = {'form':form}
    return render(request,"register.html",context)



def login(request):
    form = LoginForm()
    msg=''
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            x = Register.objects.filter(username = username,pwd = pwd).count()
            if x >0 :
                request.session['login'] =username
                return redirect('/')
            else:
                msg = "invalid"
    context = {'form':form,'msg':msg}
    return render(request,'login.html',context)


def logout(request):
    try:
        if request.method == 'GET':
           del request.session['login']
           return redirect('index')
    except KeyError:
        return redirect('/')


def add_to_cart(request,str,id):
    username = str
    print(str)
    print(id)
    veg = Vegetable.objects.get(id=id)
    name = veg.name
    quantity = veg.quantity
    price = veg.price
    image = veg.image
    cart1 = Cart.objects.filter(name=name,username=str).values()
    print(cart1)
    c= 0
    print(len(cart1))
    if len(cart1)==1:
        s = cart1[0].get('id')
        c = c+veg.quantity
        cart = Cart.objects.get(id=s)
        cart.quantity = cart.quantity+c
        print(cart.quantity)
        cart.price = veg.price*cart.quantity
        print(cart.price)
        cart.save()
        return redirect('index')
    else:
        cart = Cart(username=username,name=name,quantity=quantity,price=price,image=image)
        cart.save()
        return redirect('index')

def cartitem(request,str):
    username = str
    cart = Cart.objects.filter(username=username)
    if len(cart)==0:
        msg= "items is not available in the cart"
        return render(request,'cartitem.html',{'msg':msg})
    else:
        l = [i['quantity'] for i in cart.values() for j in i.keys() if j=="quantity"]
        print(l)
        d = [i['price'] for i in cart.values() for j in i.keys() if j=="price"]
        print(d)
        total_q = sum(l)
        total_p = sum(d)
        count = len(cart)
        context = {'cart':cart,"count":count,"total_p":total_p,"total_q":total_q,'username':username}
        return render(request,'cartitem.html',context)
    

def cartremove(request,id):
    username = request.session['login']
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('/')

def payment(request,p,q,us):
    us =us
    context = {'amount':p}
    return render(request,'payment.html',context)
