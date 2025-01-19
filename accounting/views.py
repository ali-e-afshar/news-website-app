from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.contrib.auth.forms import PasswordResetForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'accounting/register.html', {'form': form})


@login_required
def admin_dashboard(request):
    if request.user.user_type in ['SU', 'AU']:
        return render(request, 'accounting/admin_dashboard.html')
    return redirect('home')


def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'accounting/forgot_password.html', {'form': form})
