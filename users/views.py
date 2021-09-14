from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def register(request):
	"""新しいユーザーを追加する"""
	if request.method != 'POST':
		form = UserCreationForm() #空のユーザーフォーム
	else:
		form = UserCreationForm(data=request.POST) #入力済フォーム
		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			return redirect('learning_logs:index')
	context = {'form':form}
	return render(request, 'registration/register.html', context)

def user_entries(request, user_id):
	"""ユーザーの全ての記事(entry)を表示"""
	user = User.objects.get(id=user_id)
	entries = user.entry_set.order_by('-date_added')
	context = {'entries': entries}
	return render(request, 'users/user_entries.html', context)
