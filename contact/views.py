from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


def contact(request):
    if request.POST:
        to_email = settings.DEFAULT_ORDER_EMAIL
        contact_email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']

        email_context = {
            'name': name,
            'email': contact_email,
            'subject': subject,
            'message': message,
        }

        subject = render_to_string(
            'contact/contact_emails/contact_email_subject.txt',
        )

        body = render_to_string(
            'contact/contact_emails/contact_email_body.txt', email_context
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [to_email],
        )

        messages.success(request, "Your message was successfully sent! We will get back to you as soon as possible.")
        return redirect(reverse('home'))

    template = 'contact/contact.html'

    return render(request, template)
