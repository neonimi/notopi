from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import TopicForm, EntryForm, InquiryForm
from django.http import Http404
from django.views import generic #クラスベースビュー
from django.urls import reverse_lazy
from django.contrib import messages
import logging
import logging.handlers

logger = logging.getLogger(__name__) #forms.pyに記述するメール送信メソッド呼び出し


# Create your views here.
def index(request):
	return render(request, 'learning_logs/index.html')

# class IndexView(generic.TemplateView):
# 	template_name = 'index.html'

def about(request):
	return render(request, 'learning_logs/about.html')

def contact(request):
	return render(request, 'learning_logs/contact.html')

def topic(request):
	topics = Topic.objects.order_by('date_added')
	context = {'topic': topics}
	return render(request, 'learning_logs/topic.html', context)

# class TopicView(generic.ListView):
# 	model = Topic
# 	template_name = 'topic.html'
#	paginate_by = 2
	
# 	def get_queryset(self):
# 		topics = Topic.objects.order_by('date_added')

class InquiryView(generic.FormView):
	template_name = 'inquiry.html'
	form_class = InquiryForm
	success_url = reverse_lazy('learning_logs:inquiry')

	def form_valid(self, form):
		form.send_email()
		messages.success(self.request, 'メッセージを送信しました。') #メッセージ表示
		logger.info('inquiry sent by {}'.format(form.cleaned_data['name']))
		return super().form_valid(form)

def topic_child(request, topic_id):
	"""１つのトピックとそれについての全ての記事を表示"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, "learning_logs/topic_child.html", context)

@login_required
def new_topic(request):
	if request.method != 'POST':#データ送信されていない時
		form = TopicForm()#空のフォーム
	else:#データ送信された時
		form = TopicForm(data=request.POST)#データ入りフォーム
		if form.is_valid():#バリデーション
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()#保存
			return redirect('learning_logs:topic')#保存後の画面表示先
	context = {'form': form}#フォームを送る
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.owner = request.user
			new_entry.save()
			return redirect('learning_logs:topic_child', topic_id=topic_id)
	context = {'topic': topic,'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	# トピックが現在のユーザーが所持するものであることを確認する
	if entry.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid:
			form.save()
			return redirect('learning_logs:topic_child', topic_id=topic.id)

	context = {'entry': entry, 'topic':topic ,'form':form}
	return render(request, 'learning_logs/edit.html', context)