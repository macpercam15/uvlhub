from app.modules.nuevo.models import Nuevo
from core.repositories.BaseRepository import BaseRepository


class NuevoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Nuevo)

    def get_all_by_user(self, user_id):
        return Notepad.query.filter_by(user_id=user.id).all()
