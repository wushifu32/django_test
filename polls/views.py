from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
'''
def index(request):
    latest_question_list = Question.objects.order_by('-publish_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
'''
class Index(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-publish_date')[:5]

'''
def details(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': q})
    
def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': q})
'''
class Details(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class Results(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        voted_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
                'question': q,
                'error_msg': "Invalid Choice"})
    else:
        voted_choice.votes += 1
        voted_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(q.id, )))

