from django.shortcuts import render, redirect
from django.views import View
from ..models import StudentIdCard, IdCard
from django.http import HttpResponse
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
        if form.is_valid():
            instance = form.save()

            pk = instance.template_id

            side = request.POST.get('id_side')
            user_type = request.POST.get('type')

            id_card = IdCard.objects.get(pk=pk)

            id = request.POST.get('user_id')

            student = Student.objects.get(pk=id)
            teacher = Teacher.objects.get(pk=id)

            context = {
                'student': student,
                'id_card': id_card,
                'side': side,
                'teacher': teacher
            }
            if user_type == 'teacher':
                return render(request, 'idcard/teacheridcard/teacheridcard.html', context)
            elif user_type == 'staff':
                return render(request, 'idcard/staffidcard/staffidcard.html', context)
            else:
                return render(request, 'idcard/studentidcard/view_studentidcard.html', context)



