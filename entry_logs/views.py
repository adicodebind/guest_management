from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from registration.models import User, Visitor
from .forms import VisitorLogForm, CheckoutForm
from .models import VisitorLog
from .utils import send_checkin_email_to_hosts, send_checkout_email_to_visitor


# Create your views here.
@login_required
def show_logs(request):
    if not hasattr(request.user, "host"):
        return HttpResponse("Only hosts can view entry logs")

    logs = VisitorLog.objects.filter(host=request.user.host)

    return render(request, "entry_logs/all_logs.html", context={"logs": logs})


def checkin(request):
    if request.method == "POST":
        form = VisitorLogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.filter(email=data['email']).first()
            if not user:
                user = User.objects.create_user(username=data['email'], email=data['email'],
                                                phone_number=data['phone_number'])
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.save()

            if not hasattr(user, 'visitor'):
                visitor = Visitor.objects.create(user=user)

            existing_visitor = VisitorLog.objects.filter(visitor_user=user.visitor, checkout_time=None).first()
            if existing_visitor:
                form.add_error(None, "You are already checked in")
            else:
                visitor_log = VisitorLog.objects.create(visitor_user=user.visitor, checkin_time=timezone.now(), address=data['address'], host=data['host'])

                # print(visitor_log.__dict__)
                send_checkin_email_to_hosts(visitor_log)
                return render(request, "entry_logs/checkin_complete.html", context={"log": visitor_log})

    else:
        form = VisitorLogForm()

    context = {
        "form": form
    }
    return render(request, "entry_logs/checkin.html", context=context)


def checkout(request):
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            log = VisitorLog.objects.filter(visitor_user__user__email=data['email'], unique_token=data['token'],
                                            checkout_time=None).last()
            if not log:
                form.add_error(None, "No entry found with this email/token")
            else:
                log.checkout_time = timezone.now()
                log.save()
                send_checkout_email_to_visitor(log)
                return render(request, "entry_logs/checkout_complete.html", context={})

    else:
        form = CheckoutForm()

    context = {
        "form": form
    }
    return render(request, "entry_logs/checkout.html", context=context)
