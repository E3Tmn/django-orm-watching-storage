from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    active_visits = Visit.objects.filter(leaved_at=None)
    for person in active_visits:
        non_closed_visits.append(
            {
                'who_entered': f'{person.passcard}',
                'entered_at': f'{person.entered_at.strftime("%d-%m-%Y %H:%M")}',
                'duration': f'{Visit.format_duration(Visit.get_duration(person))}'
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
