from allauth.socialaccount.providers.oauth2_provider.urls import default_urlpatterns

from .provider import StripeProvider


urlpatterns = default_urlpatterns(StripeProvider)