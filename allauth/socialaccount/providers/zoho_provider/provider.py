from allauth.account.models import EmailAddress
from allauth.socialaccount.providers.base_provider import ProviderAccount
from allauth.socialaccount.providers.oauth2_provider.provider import OAuth2Provider
from allauth.socialaccount.providers.zoho_provider.views import ZohoOAuth2Adapter


class ZohoAccount(ProviderAccount):
    def to_str(self):
        dflt = super(ZohoAccount, self).to_str()
        return self.account.extra_data.get("Display_Name", dflt)


class ZohoProvider(OAuth2Provider):
    id = "zoho"
    name = "Zoho"
    account_class = ZohoAccount
    oauth2_adapter_class = ZohoOAuth2Adapter

    def get_default_scope(self):
        return ["aaaserver.profile.READ"]

    def extract_uid(self, data):
        return str(data["ZUID"])

    def extract_common_fields(self, data):
        return dict(
            email=data["Email"],
            username=data["Display_Name"],
            first_name=data["First_Name"],
            last_name=data["Last_Name"],
        )

    def extract_email_addresses(self, data):
        ret = []
        email = data.get("Email")
        if email:
            ret.append(
                EmailAddress(
                    email=email,
                    verified=False,
                    primary=True,
                )
            )
        return ret


provider_classes = [ZohoProvider]