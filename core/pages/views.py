from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum
from . models import *

def index(request):
    members = Member.objects.all()
    payments = Payment.objects.all()

    paginator = Paginator(members, 5)
    page = request.GET.get('page')
    member_listings = paginator.get_page(page)

    paginator = Paginator(payments, 5)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    total = Payment.objects.aggregate(Sum('amount'))
    total = float(sum(total.values()))

    previous = Payment.objects.filter(mode='Previous').aggregate(Sum('amount'))
    previous = float(sum(previous.values()))

    cash = Payment.objects.filter(mode='Cash').aggregate(Sum('amount'))
    cash = float(sum(cash.values()))

    misc = Payment.objects.filter(mode='Misc').aggregate(Sum('amount'))
    misc = float(sum(misc.values()))

    context = {
        'members': member_listings,
        'payments': page_listings,
        'total': total,
        'previous': previous,
        'cash': cash,
        'misc': misc,
    }
    return render(request, 'pages/index.html', context)
