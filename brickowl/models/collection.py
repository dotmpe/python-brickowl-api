from .base import BaseModel, ObjectListModel

class CollectionLots(ObjectListModel):

    def __init__(self):
        super().__init__(list=[], listObject=Lot)

class Lot(BaseModel):

    def __init__(self, con=None, ful_con=None, qty=None, lot_id=None,
            boid=None,
            note=None, price=None, type=None, ids=None):
        super().__init__()
        self.lot_id = lot_id
        self.type = type
        self.boid = boid
        self.qty = qty
        self.con = con
        self.note = note
        self.ful_con = ful_con
        self.price = price
        self.ids = ids
