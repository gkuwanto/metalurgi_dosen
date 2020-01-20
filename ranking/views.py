from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Teacher, Student
import operator

# Create your views here.


def index(request):
    teachers = Teacher.objects.order_by('id')
    students = Student.objects.order_by('-ipk')
    if len(students)==66:
        results = calculate(students, teachers)
        return render(request, 'ranking/hasil.html',{'results': results})
    return render(request, 'ranking/index.html', {'teachers': teachers})
    
def input_data(request):
    if request.method == 'GET':
        return HttpResponse('HELLO')
    elif request.method == 'POST':
        body = request.POST
        teacher = get_object_or_404(Teacher, pk=int(body['dosen']))
        student = Student.objects.create(nim=int(body['nim']), ipk=body['ipk'], pilihan=teacher)
        student.save()
    return redirect('/')

def calculate(students, teachers):
    capacities = [1 for i in teachers]
    name = [teach.name for teach in teachers]
    relations = {}
    for student in students:
        if capacities[student.pilihan_id-1] > 0:
            relations[student.nim] = name[student.pilihan_id-1]
            capacities[student.pilihan_id-1] -= 1
        else:
            buangan, _ = max(enumerate(capacities), key=operator.itemgetter(1))
            relations[student.nim] = 'Dibuang ke '+ name[buangan]
            capacities[buangan] -= 1
    return relations


    