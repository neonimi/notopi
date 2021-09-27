"""
Django settings for learning_log project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# 開発環境用
from .settings_common import *

# Security warning
DEBUG = True

# 許可するホストの設定
ALLOWED_HOSTS = []

#その他設定（ロギング、静的ファイルの配置場所、メール設定 etc.）
STATIC_ROOT = '/home/ar/web/notopi.work/static/'

# メディアファイルの保存場所
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ロギング設定（開発用）
LOGGING = {
    'version': 1, # 1固定
    'disable_existing_loggers': False, # 既存ログを無効化

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # learning_logsアプリケーションが利用するロガー
        'learning_logs': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler', # コンソールへ出力する
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'