from django.shortcuts import render, redirect
from main_page.models import Reservations, Category
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from braces.views import GroupRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .form import CategoryForm
from django.contrib import messages


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


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def list_of_categories(request):
    item = Category.objects.all().order_by('category_order')
    return render(request, 'categories.html', context={'categories': item})


class CategoryAddView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = ['manager']
    model = Category
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Category success add'
    form_class = CategoryForm
    template_name = 'category_add.html'


class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = ['manager']
    model = Category
    success_url = reverse_lazy('list_of_categories')
    success_message = 'Category success update'
    form_class = CategoryForm
    template_name = 'category_update.html'


class CategoryDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = ['manager']
    model = Category
    success_url = reverse_lazy('list_of_categories')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Category success delete!')
        return self.post(request,*args, **kwargs)




