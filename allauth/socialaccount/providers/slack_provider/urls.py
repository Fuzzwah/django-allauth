from allauth.socialaccount.providers.oauth2_provider.urls import default_urlpatterns

from .provider import SlackProvider


urlpatterns = default_urlpatterns(SlackProvider)