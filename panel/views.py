from django.shortcuts import render
from .models import Customer

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_a_customer(request):
    if request.method == 'POST':
        # Access form data directly from POST request
        customer_name = request.POST.get('customerName')
        email = request.POST.get('email')
        mobile_num = request.POST.get('mobileno')
        city = request.POST.get('city')
        # Create a new instance of Customer model and save to the database
        Customer.objects.create(
            customer_name=customer_name,
            email=email,
            mobile_num=mobile_num,
            city=city
        )

        return render('panel:index')

    return render(request, 'add_a_customer.html')