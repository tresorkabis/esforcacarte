from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib import messages

from users.models import User
from users.utils import generatePassword

class RequestAccount(View):
    
    def get(self, request):
        ctx = {
            "lrequest_account" : "active"
        }
        return render(request, 'users/requestaccount.html', ctx)

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")

        password = generatePassword()
        print(request.POST)
        rs_username = User.objects.filter(username=username)

        username = username.lower()

        if len(rs_username) > 0:
            messages.warning(request, "Ce nom utilisateur existe déjà")
        else:
            user = User(
                username = username,
                email = email,
                first_name = password
            )
            user.set_password(password)
            user.save()
      

        return HttpResponseRedirect("/")