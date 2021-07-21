from django.shortcuts import render, redirect
from main_page.models import Reservations
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def list_of_reserves(request):
    reserves = Reservations.objects.filter(is_processed=False).order_by('order_time')
    paginator = Paginator(reserves, 2)
    page = request.GET.get('page')
    reserves = paginator.get_page(page)
    return render(request, 'reserves.html', context={'reserves': reserves})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reserve(request, pk):
    Reservations.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/manager/reserve/')