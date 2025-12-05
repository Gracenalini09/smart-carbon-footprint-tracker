from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import ActivityCategory, ActivityLog
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    # Public home page – no login required
    return render(request, 'home.html')


@login_required
def add_activity(request):
    categories = ActivityCategory.objects.all()

    if request.method == "POST":
        category_id = request.POST.get("category")
        amount = request.POST.get("amount")
        date_str = request.POST.get("date")

        if date_str:
            activity_date = date.fromisoformat(date_str)
        else:
            activity_date = date.today()

        if category_id and amount:
            category = ActivityCategory.objects.get(id=category_id)
            ActivityLog.objects.create(
                user=request.user,
                category=category,
                amount=float(amount),
                date=activity_date,
            )
            return redirect("dashboard")

    return render(request, "add_activity.html", {"categories": categories})


@login_required
def activity_list(request):
    logs = ActivityLog.objects.filter(user=request.user).order_by("-date")
    return render(request, "activity_list.html", {"logs": logs})


@login_required
def dashboard(request):
    logs = ActivityLog.objects.filter(user=request.user).order_by("date")
    total_emissions = sum(log.emissions for log in logs)

    daily = {}
    for log in logs:
        key = log.date.strftime("%Y-%m-%d")
        daily[key] = daily.get(key, 0) + log.emissions

    dates = list(daily.keys())
    emissions = list(daily.values())

    context = {
        "total_emissions": total_emissions,
        "recent_logs": logs[::-1][:5],
        "dates": dates,
        "emissions": emissions,
    }
    return render(request, "dashboard.html", context)
 

def logout_view(request):
    logout(request)
    return redirect('home')