from celery import task
from django.core.mail import send_mail


@task()
def contactus_send_mail(**kwargs):
    contactus_send_email(kwargs['email'])


def contactus_send_email(*to):
    subject = 'Thank you for contacting Deepak Malik'
    body = '''
            Hello Deepak Malik,
                Thank you for sending email. I would try to responed you once it.
            '''
    frm = 'deepak@gmail.com'
    send_mail(subject, body, frm, to, fail_silently=False)
