from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    owner_name = get_object_or_404(Passcard, passcode=passcode)
    all_visit_pass = Visit.objects.filter(passcard=owner_name)
    this_passcard_visits = []
    for one_visit in all_visit_pass:
        this_passcard_visits.append(
            {
                'entered_at': one_visit.entered_at.strftime("%d-%m-%Y %H:%M"),
                'duration': Visit.format_duration(Visit.get_duration(one_visit)),
                'is_strange': Visit.is_visit_long(one_visit)
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
