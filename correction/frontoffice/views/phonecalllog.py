from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..models import Phonecalllog
from ..forms.phonecalllogform import AddPhonecalllogForm, EditPhonecalllogForm


class AllPhoneCallLogView(View):
    model = Phonecalllog
    template_name = 'phonecalllog/index.html'

    def get(self, request):
        phonecalllogs = Phonecalllog.objects.filter(active_status=2).order_by('-id')
        context = {'phonecalllogs': phonecalllogs}
        return render(request, self.template_name, context)


class AddPhoneCallLogView(View):
    model = Phonecalllog
    form_class = AddPhonecalllogForm
    template_name = 'phonecalllog/add_phonecalllog.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            phonecalllog = form.save(commit=False)
            phonecalllog.save()

            response = {
                'user': phonecalllog.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditPhoneCallLogView(View):
    model = Phonecalllog
    form_class = EditPhonecalllogForm
    template_name = 'phonecalllog/edit_phonecalllog.html'

    def get(self, request, pk, *args, **kwargs):
        phonecalllog = Phonecalllog.objects.get(pk=pk)
        form = self.form_class(instance=phonecalllog)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        phonecalllog = Phonecalllog.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=phonecalllog)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)

        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeletePhoneCallLogView(View):

    template_name = 'phonecalllog/delete_phonecalllog.html'

    def get(self, request, pk):
        phonecalllog = Phonecalllog.objects.get(pk=pk)
        context = {
            'phonecalllog': phonecalllog
        }
        return render(request, self.template_name,context)

    def post(self, request, pk, *args, **kwargs):
        phonecalllog = Phonecalllog.objects.get(pk=pk)
        phonecalllog.active_status = 0
        phonecalllog.save()

        return redirect('frontoffice:phonecalllogs')


class DetailPhoneCallLogView(View):
   pass




