from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import GetExchangeRateForm
from .models import GetExchangeRate


@login_required(login_url='/user/login')
def index(request):
 
    # return redirect(reverse('users:user_page'))
    return render(request, 'users/index.html',{'user': request.user})
    
@login_required(login_url='/user/login')
def xchange_rate(request):

    form = GetExchangeRateForm()
    rate = GetExchangeRate.objects.filter(
        user=request.user).order_by('-created_at')[:1][0].rate


    if request.method == 'POST':  
        data = {}    
        data['user'] = request.user
        data['base_currency'] = request.POST.get('base_currency')
        data['target_currency'] = request.POST.get('target_currency')
        data['amount'] = request.POST.get('amount')
        
        # form = GetExchangeRateForm(data=request.POST)
        form = GetExchangeRateForm(data=data)
  
        if form.is_valid():

            form.save()
        else:
            print(form.errors)

    context = {
        'user': request.user, 'form': form,
        'rate': rate
        }

    return render(request, 'currency_conversion_api/exchanges.html', context)