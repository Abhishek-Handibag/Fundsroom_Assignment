from django.shortcuts import render, redirect
from .forms import ShareForm
from .models import Share

def calculate_percentage_change(purchase_cost, current_cost):
    return ((current_cost - purchase_cost) / purchase_cost) * 100

def calculate_total_profit_loss(purchase_cost, current_cost, num_shares):
    return (current_cost - purchase_cost) * num_shares

def share_input(request):
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            share = form.save(commit=False)
            share.save()
            return redirect('share_input')
    else:
        form = ShareForm()
    
    shares = Share.objects.all()
    total_profit_loss = 0
    for share in shares:
        share.percentage_change = calculate_percentage_change(share.purchase_cost, share.current_cost)
        share.total_profit_loss = calculate_total_profit_loss(share.purchase_cost, share.current_cost, share.num_shares)
        total_profit_loss += share.total_profit_loss
    
    return render(request, 'stocks/share_input.html', {'form': form, 'shares': shares, 'total_profit_loss': total_profit_loss})
