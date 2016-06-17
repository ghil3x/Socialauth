from django.shortcuts import render
from allauth.account.views import ConfirmEmailView
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from allauth.socialaccount.providers.twitter.views import TwitterOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

"""
class SocialLoginView(LoginView):
    #class utilisé pour l'utilisation du social authentications pour twitter avec le access_token
    class TwitterLogin(SocialLoginView):
        adapter_class = TwitterOAuth2Adapter
        client_class = OAuth2Client
        callback_url = 'localhost:8000/accounts/twitter/callback'

    class GoogleLogin(SocialLoginView):
        adapter_class = GoogleOAuth2Adapter
        client_class = OAuth2Client
        callback_url = 'localhost:8000/accounts/google/login/callback'
"""