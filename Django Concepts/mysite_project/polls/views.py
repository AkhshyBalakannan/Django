import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django import template
from django.db.models.query_utils import Q
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
from django.db.models.functions import Lower
from django.db.models import Count

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
        # q = Question.annotate(Choice('entry'))
        # print(q.entry__choice)
        print(Question.objects.reverse()[:10])
        print(Question.objects.reverse()[:10].values())
        print(Question.objects.reverse()[:10].values('id'))
        print(Question.objects.reverse()[:10].values_list(
            'id', Lower('question_text')))
        print(Question.objects.reverse()[:10].values(
            'question_text', entries=Count('question_text')))
        print(Question.objects.reverse()[:10].values(
            lower_question=Lower('question_text')))
        print(Question.objects.defer('question_text'))
        # we use PARAMS to check properly
        Question.objects.extra(where=['question_text=%s'], params=[
                               'Hey I am question'])
        # otherwise can be used as earliest instead of lastest
        print(Question.objects.lastest('pub_date'))
        # using of ^ will some times give out NULL and that to in MySQl so filtering is best
        print(Question.objects.first())
        print(Question.objects.last())
        print(Question.objects.aggregate(Count('choice')))
        print(Question.objects.filter(pub_date__isnull=False).latest('pub_date'))
        return Question.objects.order_by('-pub_date')[:10]

# When calling save() for instances with deferred fields,
# only the loaded fields will be saved.
# Load all fields immediately.
# my_queryset.defer(None)


# Since defer() acts incrementally(adding fields to the deferred list),
# you can combine calls to only() and defer() and things will behave logically:

# Final result is that everything except "headline" is deferred.
# Entry.objects.only("headline", "body").defer("body")


# entries = Entry.objects.select_for_update().filter(author=request.user)
# with transaction.atomic():
#     for entry in entries:
#         ...

# Final result loads headline and body immediately (only() replaces any
# existing set of fields).
# Entry.objects.defer("body").only("headline", "body")

# qs1.union(qs2, qs3)
# qs1.intersection(qs2, qs3)
# qs1.difference(qs2, qs3)


# Restaurant.objects.prefetch_related('pizzas__toppings')

# This will prefetch all pizzas belonging to restaurants,
# and all toppings belonging to those pizzas.
# This will result in a total of 3 database queries - one for the restaurants,
# one for the pizzas, and one for the toppings.

# if the get doesnot find the request it raises
# Entry.objects.get(id=-999)  # raises Entry.DoesNotExist

def noUrl(request):
    '''This is an example function no url is attached to this function'''
    try:
        question_1 = Question.objects.get(id=3)
        question_2 = Question.objects.get(id=4)
    except ObjectDoesNotExist:
        print("Either the question_1 and question_2 doesn't exist.")


def nourl_tocreate(request):
    '''This is an example function no url is attached to this function'''
    p = Question.objects.create(
        question='Hey I am question')  # one step
    # Or the usual steps to be followed
    p = Question(question='Hey I am question')
    p.save(force_insert=True)


def nourl_get_or_create(request):
    '''This is an example function no url is attached to this function'''
    # Basic steps in get or create
    try:
        obj = Question.objects.get(question_text='Hwy I am question')

    except Question.DoesNotExist:
        obj = Question(question_text='Hey I am question')
        obj.save()

    # one step to get or create
    obj, created = Question.objects.get_or_create(
        question_text='Hey I am question')


def nourl_update_or_create(request):
    '''This is an example function no url is attached to this function'''
    # Basic steps in update or create
    defaults = {'question': 'Hey I have been updated'}
    try:
        obj = Question.objects.get(question_text='Hey I am question')
        for key, value in defaults.items():
            setattr(obj, key, value)
        obj.save()
    except Question.DoesNotExist:
        new_values = {'question_text': 'Hey I am question'}
        new_values.update(defaults)
        obj = Question(**new_values)
        obj.save()

    # one step
    obj, created = Question.objects.update_or_create(
        question_text='Hey I am question',
        defaults={'question': 'Hey I have been updated'},
    )


def nourl_bulk_create(request):
    '''This is an example function no url is attached to this function'''
    Question.objects.bulk_create([
        Question(question_text='Hey I am question 1'),
        Question(question_text='Hey I am question 2'),
    ])
    # This has a number of caveats though:
    # The model’s save() method will not be called,
    # and the pre_save and post_save signals will not be sent.
    # It does not work with child models in a multi-table inheritance scenario.
    # If the model’s primary key is an AutoField, the primary key attribute
    # can only be retrieved on certain databases (currently PostgreSQL and MariaDB 10.5+).
    # On other databases, it will not be set.
    # It does not work with many-to-many relationships.
    # It casts objs to a list, which fully evaluates objs if it’s a generator.


def nourl_bulk_update(request):
    '''This is an example function no url is attached to this function'''
    # SAME CAVEATS ARE HERE AS ABOVE
    objs = [
        Question.objects.create(question_text='Hey I am question 1'),
        Question.objects.create(question_text='Hey I am question 2'),
    ]
    objs[0].question_text = 'This is entry 1'
    objs[1].question_text = 'This is entry 2'
    Question.objects.bulk_update(objs, ['question_text'])


def nourl_exists(request):
    '''This is an example function no url is attached to this function'''
    # usual steps **
    question = Question.objects.get(pk=123)
    if Question.filter(pk=question.pk).exists():
        print("Entry contained in queryset")

    # faster way will be
    if question in Question:
        print("Entry contained in QuerySet")

    # one step method will be
    if Question.exists():
        print("There is at least one object in some_queryset")


def nourl_exact_iexact(request):
    '''This is an example function no url is attached to this function'''
    # exact match
    Question.objects.get(id__exact=14)
    Question.objects.get(id__exact=None)
    # SELECT ... WHERE id = 14;

    # iexact match case insensitive
    Question.objects.get(name__iexact='beatles blog')
    Question.objects.get(name__iexact=None)
    # SELECT ... WHERE name ILIKE 'beatles blog';


def nourl_contains_icontains(request):
    '''This is an example function no url is attached to this function'''
    Question.objects.get(question_text__contains='Hey I am question')
    # SELECT ... WHERE question_text LIKE '%Hey i am question%';

    Question.objects.get(question_text__icontains='Hey I am question')
    # SELECT ... WHERE question_text ILIKE '%Hey I am question%';


def nourl_common(request):
    '''This function is example which is not attached
    with any urls and this consists of all commonly used querysets '''
    Question.objects.filter(id__in=[1, 3, 4])
    Question.objects.filter(id__gt=4)
    Question.objects.filter(question_text__startswith='Hey')
    Question.objects.filter(question_text__istartswith='hey')
    Question.objects.filter(question_text__endswith='question')
    Question.objects.filter(question_text__iendswith='Question')
    # import datetime
    Question.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
    Question.objects.filter(pub_date__year=2005)
    Question.objects.filter(pub_date__iso_year__gte=2005)
    Question.objects.filter(pub_date__month=12)
    Question.objects.filter(pub_date__day__gte=3)
    Question.objects.filter(pub_date__week__gte=32, pub_date__week__lte=38)
    Question.objects.filter(pub_date__week_day__gte=2)
    Question.objects.filter(pub_date__time=datetime.time(14, 30))
    Question.objects.filter(timestamp__hour=23)
    Question.objects.filter(time__hour=5)
    Question.objects.get(question_text__regex=r'^(An?|The) +')
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets


def tags(request):
    return render(request, 'polls/built_in_tags.html')


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


# qs1 = Author.objects.values_list('name')
# qs2 = Entry.objects.values_list('headline')
# qs1.union(qs2).order_by('name')

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
        selected_choice = question.choice_set.get(
            pk=request.POST['choice'])
        selected_choice.repr()
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
