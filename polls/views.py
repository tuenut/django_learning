from django.shortcuts import render

# Create your views here.


def polls_list(request):
    context = {'polls_list': list()}
    return render(request, 'polls/list.html', context)
