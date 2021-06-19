from django.shortcuts import render
from .forms import ContactForm
from main.models import Customer, Cart

def support_page(request):
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(owner=customer)
    context = {
            'cart':cart,
        }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form,
               'cart': cart,
               }
    return render(request, "support.html", context)
