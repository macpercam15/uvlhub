from app.modules.nuevo.repositories import NuevoRepository
from core.services.BaseService import BaseService


class NuevoService(BaseService):
    def __init__(self):
        super().__init__(NuevoRepository())
    
    def get_all_by_user(self, user_id):
        return self.repository.get_all_by_user(user_id)
