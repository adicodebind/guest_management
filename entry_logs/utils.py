from django.conf import settings
from django.template.loader import render_to_string

from base.utils import send_email_wrapper, run_in_background
from registration.models import Host


@run_in_background
def send_checkin_email_to_hosts(entry_log):
    receivers = [entry_log.host.user.email]
    message = render_to_string('entry_logs/email_templates/checkin_email.html', {"log": entry_log})
    subject = "New Entry at Entry Gate"
    send_email_wrapper(sender=settings.DEFAULT_EMAIL_SENDER, receivers=receivers, subject=subject, message=message)


@run_in_background
def send_checkout_email_to_visitor(entry_log):
    receivers = [entry_log.visitor_user.user.email]
    message = render_to_string('entry_logs/email_templates/checkout_email.html', {"log": entry_log})
    subject = "Thank you for visiting this organization"
    send_email_wrapper(sender=settings.DEFAULT_EMAIL_SENDER, receivers=receivers, subject=subject, message=message)
