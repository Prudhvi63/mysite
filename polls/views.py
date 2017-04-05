from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    last_five_questions = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':last_five_questions,
    }
    return render(request,'polls/index.html',context)

def home(request):
     return  HttpResponse("This is the home page")

def detail(request,question_id):
    question  = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question,})

def result(request,question_id):
    result1 = "You are looking at the result of the quetion %s"
    return HttpResponse(result1 % question_id)
def vote(request,question_id):
    return HttpResponse("You are now voting for question %s" % question_id)
