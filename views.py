from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from .models import User

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_users')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})

def view_users(request):
    users = User.objects.all()
    return render(request, 'users/view_users.html', {'users': users})

def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_users')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/edit_user.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('view_users')
    return render(request, 'users/delete_confirmation.html', {'user': user})
