from django.shortcuts import render,redirect
from .forms import CreateUserForm,CreateProductForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Products,CartItem
# Create your views here.

def index(request):
    return render(request, 'index.html')

def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST) 
     
        if form.is_valid():
            form.save()
            return redirect('login')
            
            
   
    return render(request, 'register.html', {'form': form})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('shop')
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop')
        else : 
            messages.info(request, 'User or password not correct!')
    
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def createProducts(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProductForm()
        
       
    return render(request, 'createProduct.html', {'form': form})


def shopPage(request):
    products = Products.objects.all()
    
    context = {'products': products}
    return render(request, 'shop.html', context)


def productDetail(request, id):
    product = Products.objects.get(id=id)
    context = {'product': product}
    
    return render(request, 'detail.html', context)

def addToCart(request, id):
   if request.user.is_authenticated :
        product = Products.objects.get(id=id)
        cart, created = CartItem.objects.get_or_create(user_id=request.user.id, product_id= id)
        print(created)
        if created :
            cart.quantity = 1 
            cart.total = product.price
            cart.save()
        else :
            cart = CartItem.objects.get(user_id=request.user.id, product_id= id)
            cart.quantity += 1
            cart.total = cart.quantity * product.price
            cart.save()
        
        return redirect('cart')
   else :
       return redirect('login')
    

def carts(request):
    if request.user.is_authenticated :
        carts = CartItem.objects.filter(user_id=request.user.id).select_related('product')
        cart_list = [
        {
        'product_id': cart.product_id,
        'quantity': cart.quantity,
        'total': cart.total,
        'title': cart.product.title,
        'price': cart.product.price,
        }
        for cart in carts
        ]
        
        context = {'cart':cart_list}
        return render(request, 'cart.html', context)
    else :
        return redirect('login')
   
