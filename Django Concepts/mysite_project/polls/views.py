from django import template
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from .models import Question, Choice, Author
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .forms import To_create_form
# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.") # BASIC RETURN

#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)                                           # RETURN WITHOUT DATA

#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))                # REURN WITH DYNAMIC DATA

#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     # DYNAMIC SHORTHAND OF RENDER
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)

#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question}) # Normal 404 page

#     question = get_object_or_404(Question, pk=question_id)
#     # Shorthand 404 page
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'polls/index_question.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class ViewChoice(generic.ListView):
    template_name = 'polls/index_choice.html'
    context_object_name = 'choices'

    def get_queryset(self):
        return Choice.objects.all()


class DetailViewChoice(generic.DetailView):
    model = Choice
    template_name = 'polls/detail_choice.html'


class AuthorCreate(CreateView):
    model = Author
    fields = ['name']


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class Set_ques(View):
    def get(self, request):
        return render(request, 'polls/questions.html')

    def post(self, request):
        question = request.POST['question_text']
        print(question)
        question_model = Question(
            question_text=question, pub_date=timezone.now())
        question_model.save()
        return HttpResponseRedirect(reverse('polls:index'))
