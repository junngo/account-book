from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Account

@login_required
def index_acc(request):
    if request.method == "POST":
        user = request.user
        name = request.POST['name']
        pub_date = request.POST['pub_date']

        account = Account(
            user = user,
            name = name,
            pub_date = pub_date,
        )
        account.save()

        account_list = Account.objects.filter(user = user)
        context = {'account_list': account_list,}

        return render(request, 'account/index_account.html', context)
    else:
        # account_list = Account.objects.get(user = request.user)
        account_list = Account.objects.filter(user = request.user)
        context = {'account_list': account_list,}

        return render(request, 'account/index_account.html', context)
