from allauth.socialaccount.providers.oauth2_provider.urls import default_urlpatterns

from .provider import FigmaProvider


urlpatterns = default_urlpatterns(FigmaProvider)