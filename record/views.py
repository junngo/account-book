from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from account.models import Account, Transaction

# Create your views here.

# to-do: 
# make helper function: When call index_record function, helper return tr data for context

@login_required
def index_record(request):

    if request.method == "POST":
        accountName = request.POST['accountName']
        trDate = request.POST['trDate']
        detail = request.POST['detail']
        price = request.POST['price']
        memo = request.POST['memo']

        account = Account.objects.get(user = request.user, 
                                      name = accountName
                                     )

        tr = Transaction(
            account = account,
            tr_date = trDate,
            tr_detail = detail,
            tr_amount = price,
            tr_memo = memo,
        )
        tr.save()

        context = {}
        return render(request, 'record/index.html', context)

    else:
        template = loader.get_template('record/index.html')
        context = {}

        return HttpResponse(template.render(context, request))
