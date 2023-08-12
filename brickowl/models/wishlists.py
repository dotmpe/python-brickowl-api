from .base import BaseModel, ObjectListModel

class WishlistList(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=Wishlist)

class Wishlist(BaseModel):

    def __init__(self, wishlist_id=None, name=None, description=None,
            public=None, url=None, item_count=None, lot_count=None,
            created=None, updated=None):
        super().__init__()
        self.wishlist_id = wishlist_id
        self.name = name
        self.description = description
        self.public = public
        self.url = url
        self.item_count = item_count
        self.lot_count = lot_count
        self.created = created
        self.updated = updated
