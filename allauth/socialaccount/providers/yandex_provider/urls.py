from allauth.socialaccount.providers.oauth2_provider.urls import default_urlpatterns

from .provider import YandexProvider


urlpatterns = default_urlpatterns(YandexProvider)