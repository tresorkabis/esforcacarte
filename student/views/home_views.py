from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        ctx = {
            "lhome" : "active"
        }
        return render(request, "home/index.html", ctx)