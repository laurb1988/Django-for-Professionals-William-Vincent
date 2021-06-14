import stripe
from django.conf import settings
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
from django.shortcuts import render
# Create your views here.


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

    
def charge(request):
    permission = Permission.objects.get(codename='special_status')
    u = request.user
    u.user.permission.add(permission)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 3900,
            currency = 'usd',
            description = 'Purchase all books',
            source = request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')