from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader 
from django.urls import reverse

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list}
    #output = '.'.join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html',context )
    #return HttpResponse("Hi iam Here")

# Create your views here.
def details(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    #question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/details.html',{'question':question})
    #return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    #response="You're looking at the results of question %s"
    return render(request,'polls/results.html',{'question':question}) #HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html',{
            'question':question,
            'error':'You didnot select a choice',
            })
    else:
        selected_choice.votes+=1
        selected_choice.save() # Call the real save() method
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
       #return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


#question = get_object_or_404(Question, pk= question_id)
    #try:
        #selected_choice = question.choice_set.get(pk = request.POST['choice'])
        #except(KeyError, Choice.DoesNotExist):
        #except (KeyError, Choice.DoesNotExist):