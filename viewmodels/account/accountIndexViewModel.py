from services import user_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class accountIndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.user = user_service.find_user_by_id(self.user_id)
        self.name = self.request_dict.name.strip()
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        pass
