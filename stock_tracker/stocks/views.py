from django.shortcuts import render, redirect
from .forms import ShareForm
from .models import Share

def calculate_percentage_change(purchase_cost, current_cost):
    return ((current_cost - purchase_cost) / purchase_cost) * 100

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
    for share in shares:
        share.percentage_change = calculate_percentage_change(share.purchase_cost, share.current_cost)
    
    return render(request, 'stocks/share_input.html', {'form': form, 'shares': shares})
