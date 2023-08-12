from .base import BaseModel, ObjectListModel

class UserDetails(BaseModel):
    def __init__(self,
        username=None,
        uid=None,
        has_store=None,
        **kwds
    ):
        super().__init__()
        self.uid = uid
        self.username = username
        self.has_store = has_store
