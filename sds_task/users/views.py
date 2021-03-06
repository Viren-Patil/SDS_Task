from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    # This method validates the filled form and then sends a mail of success if successful registration happens.
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            subject = 'Congratulations ' + save_it.first_name + '!'
            message = 'Thank You ' + save_it.username +' !\nYou have successfully registered with us!!\nEnjoy and make full use of our app.\n\nNOTE: The default color theme of the app is dark. You can change the theme from your profile.\n\nRegards,\nTeam MUSIFY'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]

            send_mail(subject, message, from_email, to_list, fail_silently=True)

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required             # Decorator used so that only authenticated user can view this page.
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
       u_form = UserUpdateForm(instance=request.user)
       p_form = ProfileUpdateForm(instance=request.user.profile) 

    context = {
        'u_form':  u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

def display_username(request):
    return render(request, 'users/display_username.html')
