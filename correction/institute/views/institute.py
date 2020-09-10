import datetime
from django.shortcuts import render
from django.utils import formats
from django.views import View
from ..models import *


class AllInstituteView(View):
    model = Institute
    template_name = 'announcement/notice/index.html'

    def get(self, request):
        notices = Institute.notices.filter(active_status=2).order_by('-id')
        date = formats.date_format(datetime.datetime.now().date(), 'd-m-Y')
        context = {'notices': notices, 'date': date}
        return render(request, self.template_name, context)
