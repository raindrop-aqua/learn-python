from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from models import Question
from forms import QuestionForm


def index(request):
    questions = Question.objects.all()
    return render_to_response('questionsandanswers/index.html',
                              {'questions': questions},
                              context_instance=RequestContext(request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render_to_response('questionsandanswers/detail.html',
                              {'question': question},
                              context_instance=RequestContext(request))


@login_required
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuestionForm()
    return render_to_response('questionsandanswers/create.html',
                              {'form': form},
                              context_instance=RequestContext(request))


@login_required
def edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuestionForm(instance=question)
    return render_to_response('questionsandanswers/edit.html',
                              {'form': form},
                              context_instance=RequestContext(request))
