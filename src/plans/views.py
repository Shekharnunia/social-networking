from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Plan, UserPlan


def plans(request):
    user = request.user
    user_plan = user.userplan.plan
    if user.status_like.count() >= user_plan.likes or user.statuscomment_set.count() < user_plan.status or user.statuscomment_set.count() < user_plan.comments:
        plans = Plan.objects.all()
        if request.method == 'POST':
            if request.POST.get('plan') is not None:
                userplan = UserPlan.objects.get(user=user)
                form_plan = Plan.objects.get(plan=request.POST.get('plan'))
                userplan.plan = form_plan
                userplan.save()
                message = ("You successfully subscribed to {}".format(userplan.plan))
                messages.success(request, message)
                return redirect('posts:list')
        return render(request, 'plans/plans.html', {'plans': plans})
    else:
        return redirect('posts:list')
