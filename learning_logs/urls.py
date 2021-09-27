from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import static

# from . import settings_common, settings_dev

app_name = 'learning_logs'
urlpatterns = [
	path('', views.index, name='index'),
	# path('', views.IndexView.as_view(), name='index'),
	#全てのトピックを表示する
	path('topic/', views.topic, name='topic'),
	#個別トピックの詳細ページ
	path('topic/<int:topic_id>/', views.topic_child, name='topic_child'),
	#新しいトピック作成ページ
	path('new_topic/', views.new_topic, name='new_topic'),
	#新しい記事作成ページ
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	#ユーザーが追加した記事(entry)の編集ページ
	path('edit/<int:entry_id>/', views.edit, name='edit'),
	#about
	path('about/', views.about, name='about'),
	#contact
	path('contact/', views.contact, name='contact'),
	# 問い合わせ
	path('inquiry/', views.InquiryView.as_view(),name="inquiry"),
]

# 開発サーバーでメディアを配信可能にする設定
# urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)