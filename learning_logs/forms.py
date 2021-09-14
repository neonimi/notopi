from django import forms
from .models import Topic, Entry
from django.core.mail import EmailMessage

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''} #ラベルを生成しない指示

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols':80})}

class InquiryForm(forms.Form):
	name = forms.CharField(label='お名前', max_length=30)
	email = forms.EmailField(label='メールアドレス')
	title = forms.CharField(label='タイトル',max_length=30)
	message = forms.CharField(label='メッセージ',widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['name'].widget.attrs['class'] = 'form-control col-9'
		self.fields['name'].widget.attrs['placeholder'] = 'お名前'
		self.fields['email'].widget.attrs['class'] = 'form-control col-11'
		self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'
		self.fields['title'].widget.attrs['class'] = 'form-control col-11'
		self.fields['title'].widget.attrs['placeholder'] = 'タイトル'
		self.fields['message'].widget.attrs['class'] = 'form-control col-12'
		self.fields['message'].widget.attrs['placeholder'] = '問い合わせ内容をここに入力してください'

	def send_email(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		title = self.cleaned_data['email']
		message = self.cleaned_data['message']

		subject = 'お問い合わせ{}'.format(title)
		message = '送信者名：{0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
		from_email = 'aaa@aaa.com'
		to_list = [#問い合わせメールの宛先一覧(to)
			'test@example.ccom'
		]
		cc_list = [#問い合わせメールの宛先一覧(cc)
			email
		]

		message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list) #EmailMessageインスタンス生成
		message.send() #メール送信