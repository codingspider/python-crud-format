from django.views import View
from django.shortcuts import render, redirect


class AddAdmitCardView(View):

    def get(self, request):
        return render(request, 'admitcard/index.html')
