from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visit_pass = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for one_visit in all_visit_pass:
        this_passcard_visits.append(
            {
                'entered_at': one_visit.entered_at.strftime("%d-%m-%Y %H:%M"),
                'duration': Visit.format_duration(one_visit.get_duration()),
                'is_strange': one_visit.is_visit_long()
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
