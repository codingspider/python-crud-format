from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..models import Phonecalllog
from ..forms.forms import PhonecalllogForm


class AllPhoneCallLogView(View):
    model = Phonecalllog
    template_name = 'phonecall/index.html'

    def get(self, request):
        phone_calls = Phonecalllog.objects.filter(active_status=2).order_by('-id')
        context = {'phone_calls': phone_calls}
        return render(request, self.template_name, context)


class AddPhoneCallLogView(View):
    model = Phonecalllog
    form_class = PhonecalllogForm
    template_name = 'phonecall/add_phone_call_log.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            phone_call_log = form.save(commit=False)
            phone_call_log.save()

            response = {
                'user': phone_call_log.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditPhoneCallLogView(View):
    model = Phonecalllog
    form_class = PhonecalllogForm
    template_name = 'phonecall/edit_phone_call_log.html'

    def get(self, request, pk, *args, **kwargs):
        phone_log = Phonecalllog.objects.get(pk=pk)
        form = self.form_class(instance=phone_log)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        phone_log = Phonecalllog.objects.get(pk=pk)
        form = self.form_class(request.POST,request.FILES, instance=phone_log)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeletePhoneCallLogView(View):

    template_name = 'phonecall/delete_phone_call_log.html'

    def get(self, request, pk):
        complain = Phonecalllog.objects.get(pk=pk)
        context ={
            'complain': complain
        }
        return render(request, self.template_name,context)

    def post(self, request, pk, *args, **kwargs):
        notice = Phonecalllog.objects.get(pk=pk)
        notice.active_status = 0
        notice.save()

        return redirect('frontoffice:phonecalllogs')


class DetailPhoneCallLogView(View):
    def get(self, request, pk):
        phonecalllog = Phonecalllog.objects.get(id=pk)
        context = {'phonecalllog': phonecalllog}
        return render(request, 'phonecall/phone_call_log_detail.html', context)





