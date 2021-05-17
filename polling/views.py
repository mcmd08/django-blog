from django.shortcuts import render
from django.http import Http404
from polling.models import Poll

# Create your views here.
def list_view(request):
    print('list_view request is:', request)
    print('list view poll obj is:', Poll.objects.all())
    print('poll obj type is:', type(Poll.objects.all()))
    print('poll obj type len is:', len(Poll.objects.all()))
    context = {'polls': Poll.objects.all()}
    print('list_view context is:', context)
    return render(request, 'polling/list.html', context)

def detail_view(request, poll_id):
    print('detail view request:', request)
    print('detail view poll_id:', poll_id)
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExit:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)
