from django.shortcuts import render, get_object_or_404
from .models import Reservation
from datetime import date, timedelta
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReservationForm

def schedule_view(request):
    # 獲取今天和未來兩週的日期範圍
    today = date.today()
    dates = [today + timedelta(days=i) for i in range(14)]
    time_slots = ["8:00–10:00", "10:00–12:00", "13:00–15:00", "15:00–17:00"]

    # 查詢所有預約
    reservations = Reservation.objects.filter(date__range=[today, dates[-1]])

    # 將時段數據轉換為列表結構
    schedule = [
        {
            'date': d,
            'slots': [
                {
                    'time_slot': slot,
                    'reservation': reservations.filter(date=d, time_slot=slot).first()
                }
                for slot in time_slots
            ]
        }
        for d in dates
    ]

    return render(request, 'schedule.html', {
        'schedule': schedule,
        'time_slots': time_slots,
    })

def reserve_slot(request, date, time_slot):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.date = date
            reservation.time_slot = time_slot
            reservation.save()
            return HttpResponseRedirect(reverse('schedule'))
    else:
        form = ReservationForm()

    return render(request, 'reserve.html', {
        'form': form,
        'date': date,
        'time_slot': time_slot,
    })
