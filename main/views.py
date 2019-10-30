from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index_main(request):
    
    context = {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Redirect to a success page.
            return HttpResponseRedirect(reverse('record:indexRecord'))

        else:
            logout(request)
            # Return an 'invalid login' error message.
            return render(request, 'main/index.html', context)

    else:
        return render(request, 'main/index.html', context)
