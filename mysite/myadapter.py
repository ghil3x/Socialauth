from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.signals import user_signed_up
from allauth.account.adapter import get_adapter
class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    #def save_user(self, request, sociallogin):
    def save_user(self, request, sociallogin, form=None):
        #Check for extra user data and save the desired fields.
        data = sociallogin.account.extra_data
        user = sociallogin.user
        if 'name' in data:
            user.name = data['name']
        elif 'first_name' in data:
            user.name = data['first_name']+data['last_name']
        if 'screen_name' in data:
            user.username = data['screen_name']
        elif 'username' in data:
            user.username = data['username']
        user.save()
        get_adapter().populate_username(request, user)
        user.set_unusable_password()
        if form:
            get_adapter().save_user(request, user, form)
        else:
            get_adapter().populate_username(request, user)
        sociallogin.save(request)
        return user
