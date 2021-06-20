from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url="/login/")
def minting_burning(request):
    if request.method == 'POST':
        return redirect('minting_burning')
    context = {}
    return render(request, "tokenised/minting_burning.html", context)


@login_required(login_url="/login/")
def inventory(request):
    if request.method == 'POST':
        return redirect('inventory')
    context = {}
    return render(request, "tokenised/inventory.html", context)

@login_required(login_url="/login/")
def profit_loss(request):
    if request.method == 'POST':
        return redirect('profit_loss')
    context = {}
    return render(request, "tokenised/profit_loss.html", context)









