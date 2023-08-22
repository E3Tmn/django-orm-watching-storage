from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    active_pass = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active_pass,
    }
    return render(request, 'active_passcards.html', context)
