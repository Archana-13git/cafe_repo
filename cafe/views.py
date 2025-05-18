
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from .forms import SignUpForm, OrderForm
from .models import MenuItem, Category, Order
import logging
from django.http import HttpResponse


logger = logging.getLogger(__name__)

def home_view(request):
    return render(request, 'cafe/home.html')

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'cafe/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'cafe/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def menu_view(request):
    categories = Category.objects.all().prefetch_related('menuitem_set')
    return render(request, 'menu.html', {'categories': categories})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # Optional email logic here
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def order_success(request):
    return render(request, 'order_success.html')

def place_order_view(request):
    items = MenuItem.objects.all()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'place_order.html', {'form': form, 'items': items})

def reserve_table(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            date = request.POST['date']
            time = request.POST['time']
            guests = request.POST['guests']
            requests_note = request.POST.get('requests', '')

            # Optional: Save reservation or send email
            send_mail(
                subject='Café Royale Reservation Confirmed ✅',
                message=f'''Hi {name},

Thank you for reserving a table at Café Royale!

📅 Date: {date}
⏰ Time: {time}
👥 Guests: {guests}

We look forward to serving you! ☕
- Café Royale
''',
                from_email='caferoyalelive@gmail.com',
                recipient_list=[email],
                fail_silently=False
            )

            return render(request, 'reservation.html')

        return render(request, 'reservation.html')

    except Exception as e:
        logger.error(f"Error occurred in reserve_table: {str(e)}")
        return HttpResponse("There was an error with your reservation.", status=500)



import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseBadRequest
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            payment_amount = 50000  # Amount in paise (e.g., ₹500)
            payment_currency = 'INR'
            payment_receipt = 'order_rcptid_11'

            order_data = {
                'amount': payment_amount,
                'currency': payment_currency,
                'receipt': payment_receipt,
                'payment_capture': '1'
            }

            order = client.order.create(data=order_data)
            context = {
                'order_id': order['id'],
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
                'amount': payment_amount
            }
            return render(request, 'payment.html', context)
        except Exception as e:
            logger.error(f"Error in create_order: {str(e)}")
            return HttpResponseBadRequest("An error occurred while creating the order.")
    return render(request, 'place_order.html')

@csrf_exempt
def payment_success(request):
    return render(request, 'payment_success.html')



