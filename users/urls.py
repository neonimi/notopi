"""users用URLパターン定義"""

from django.urls import path, include
from . import views

# Create your views here.
app_name = 'users'

urlpatterns = [
	#デフォルトの認証URLを取り込む
	path('', include('django.contrib.auth.urls')),
	#ユーザー登録ページ
	path('register/', views.register, name='register'),
	#ユーザーの記事一覧ページ
	path('entries/<int:user_id>/', views.user_entries, name='user_entries'),
]