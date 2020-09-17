from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..forms.certificatetypeform import AddCertificateTypeform, EditCertificateTypeform
from ..models import CertificateType


class AllCertificateTypeView(View):
    model = CertificateType
    template_name = 'certificate/certificatetype/index.html'

    def get(self, request):
        certificatetypes = CertificateType.objects.filter(active_status=2).order_by('-id')
        context = {'certificatetypes': certificatetypes}
        return render(request, self.template_name, context)


class AddCertificateTypeView(View):
    model = CertificateType
    form_class = AddCertificateTypeform
    template_name = "certificate/certificatetype/add_certificatetype.html"

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            certificatetype = form.save(commit=False)
            certificatetype.save()
            response = {
                'user': certificatetype.pk,
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class EditCertificateTypeView(View):
    model = CertificateType
    form_class = EditCertificateTypeform
    template_name = 'certificate/certificatetype/edit_certificatetype.html'

    def get(self, request, pk, *args, **kwargs):
        certificatetype = CertificateType.objects.get(pk=pk)
        form = self.form_class(instance=certificatetype)
        context = {'form': form, 'pk': pk}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        certificatetype = CertificateType.objects.get(pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=certificatetype)

        if form.is_valid():
            form.save()
            response = {
                'success': 'Success! '
            }
            return JsonResponse(response)
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})


class DeleteCertificateTypeView(View):
    template_name = 'certificate/certificatetype/delete_certificatetype.html'

    def get(self, request, pk):
        certificatetype = CertificateType.objects.get(pk=pk)
        context = {
            'certificatetype': certificatetype
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        certificatetype = CertificateType.objects.get(pk=pk)
        certificatetype.active_status = 0
        certificatetype.save()
        return redirect('certificate:certificatetypes')

