from django.shortcuts import render

from polls.models import Poll


def polls_list(request):
    context = {'polls_list': Poll.objects.all()}
    return render(request, 'polls/list.html', context)
