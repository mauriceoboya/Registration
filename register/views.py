from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from register.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('admin')
    else:
        form = SignUpForm()
    context = {
        'form': form

    }
    return render(request, 'registration/signup.html', context)


@login_required
def admin(request):

    return render(request, 'admin/home.html')

