from pypi_org.services import user_service
from pypi_org.services.user_service import find_user_by_email
from pypi_org.templates.viewmodels.shared.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = user_service.find_user_by_id(self.user_id)
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.name or not self.name.strip():
            self.error = 'A man needs a name'
        elif not self.email or not self.email.strip():
            self.error = 'email required'
        elif not self.password:
            self.error = 'Must specify a password'
        elif len(self.password.strip())<5:
            self.error = 'password must be 5 chars or more'
        elif find_user_by_email(self.email):
            self.error = 'A user has already registered with that email'

