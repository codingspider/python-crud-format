from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from ..forms.certificatetypeform import AddCertificateTypeform, EditCertificateTypeform
from ..models import CertificateType
from subject.models import Class
from student.models import Student
from idcard.models import IdCard


class AllCertificateView(View):
    template_name = "certificate/certificate/index.html"

    def get(self, request):
        certifactetypes = CertificateType.objects.filter(active_status=2).order_by('-id')
        classes = Class.objects.all()
        context = {'certifactetypes': certifactetypes, 'classes': classes}
        return render(request, self.template_name, context)


class AllStudentGetView(View):
    def post(self, request):
        pk = request.POST.get('class_id')
        id = request.POST.get('certificate_type_id')

        students = Student.objects.filter(pk=pk)
        certificatetype = CertificateType.objects.get(pk=id)

        certifactetypes = CertificateType.objects.filter(active_status=2).order_by('-id')
        classes = Class.objects.all()

        print(certificatetype.id)
        context = {
            'students': students,
            'certifactetypes': certifactetypes,
            'classes': classes,
            'types': certificatetype
        }
        return render(request, 'certificate/certificate/index.html', context)


class GenerateCertificateView(View):
    def get(self, request, pk, types):
        student = Student.objects.get(pk=pk)
        certificate = CertificateType.objects.get(pk=types)
        card = IdCard.objects.get(pk=3)

        context = {
            'student': student,
            'certificate': certificate,
            'card': card
        }
        return render(request, 'certificate/certificate/view_certificate.html', context)
