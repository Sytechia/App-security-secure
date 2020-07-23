from services import user_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        # self.user = user_service.find_user_by_id(self.user_id)
        self.name = self.request_dict.name.strip()
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.name:
            self.error = 'You must specify a name.'
        if not self.email or not self.email.strip():
            self.error = 'You must specify a email.'
        elif not self.password:
            self.error = 'You must specify a password.'


