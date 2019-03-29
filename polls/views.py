from django.shortcuts import render, get_object_or_404

from polls.models import Poll


def polls_list(request):
    context = {'polls_list': Poll.objects.all()}
    return render(request, 'polls/list.html', context)

def poll_page(request, poll_id):
    context = {'poll': get_object_or_404(Poll, pk=poll_id)}
    return render(request, 'polls/poll_page.html', context)
