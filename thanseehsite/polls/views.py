from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, DetailView
from .models import Question


def index(request):
    return HttpResponse("Hello, thanseeh . You're at the polls index.")


def home(request):
    return HttpResponse("Hello, thanseeh . You're at the polls home."
                        "wlcome user")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


class TestView(DetailView):
    model = Question
    template_name = 'index.html'
    context_object_name = 'question'


def page(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # list home comprehenssion
    # r = b if a > b else b
    # if a is True:
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def display(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('replay.html')
    context = {
            'latest_question_list': latest_question_list,
             }
    return HttpResponse(template.render(context, request))
