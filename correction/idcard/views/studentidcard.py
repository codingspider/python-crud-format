from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from ..models import StudentIdCard, IdCard
from ..forms.studentidform import AddStudentIdForm
from student.models import Student
from teacher.models import Teacher


class AllStudentIdCardView(View):
    model = StudentIdCard
    template_name = 'idcard/studentidcard/index.html'

    def get(self, request):
        studentidcards = StudentIdCard.objects.all().order_by('-id')
        context = {'studentidcards': studentidcards}
        return render(request, self.template_name, context)


class AddStudentIdCardView(View):
    model = StudentIdCard
    form_class = AddStudentIdForm
    template_name = 'idcard/studentidcard/add_studentidcard.html'

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        return_form = self.form_class
        if form.is_valid():
            instance = form.save()
            pk = instance.template_id
            side = request.POST.get('id_side')
            user_type = request.POST.get('type')
            id_card = IdCard.objects.filter(pk=pk).values()
            id = request.POST.get('user_id')
            queryset = Student.objects.filter(pk=id).values()
            teacher = Teacher.objects.filter(pk=id)

            data = {
                'student': queryset,
                'id_card': id_card,
                'teacher': teacher,
            }
            return JsonResponse({'data': list(queryset), 'id_card': list(id_card)})
        else:
            return JsonResponse({"error": form.errors}, json_dumps_params={'indent': 2})





