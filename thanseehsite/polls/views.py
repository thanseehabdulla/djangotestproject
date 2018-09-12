from django.http import HttpResponse


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