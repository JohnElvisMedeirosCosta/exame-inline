from django.shortcuts import render

# Create your views here.

def exam_list(request):
    template_name = 'exam/exam_list.html'
    return render(request, template_name)