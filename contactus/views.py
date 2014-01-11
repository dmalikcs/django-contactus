from django.http import HttpResponse, Http404
from contactus.models import ContactUsForm

from .tasks import contactus_send_mail


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            contactus_send_mail.apply_async(
                kwargs={
                    'email': form.cleaned_data['email']
                }
            )
            return HttpResponse('sent')
        else:
            return HttpResponse("failed")
    else:
        raise Http404
