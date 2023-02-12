from django.shortcuts import render
from django.views import View

# Create your views here.


class DashboardView(View):
    def get(self, request):

        return render(request, "dashboard-company.html")


class RequestsView(View):
    def get(self, request):

        return render(request, "requests-company.html")
