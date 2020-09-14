from django.shortcuts import render, redirect
from django.views import View
from ..models import IdCard
from django.http import HttpResponse
from ..forms.idcardform import IdCardForm


class AllStudentIdCardView(View):
    model = IdCard
    template_name = 'idcard/idcard/idcard_index.html'

    def get(self, request):
        idcards = IdCard.objects.all().order_by('-id')
        context = {'idcards': idcards}
        return render(request, self.template_name, context)


class AddIdCardView(View):
    model = IdCard
    form_class = IdCardForm
    template_name = 'idcard/idcard/id_card.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/idcard/add_idcard/')
        else:
            return HttpResponse('Something went wrong.')



