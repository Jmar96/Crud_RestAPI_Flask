from ..models import Badyet_Items
from sqlalchemy import func
from .. import db

class query_hlpr:
    def __init__(self):
        pass

    def execute():
        print(f"Query_Helpr executed..")


def get_all_items(categry=None):
    items = []
    if categry == None or categry == "":
        items = Badyet_Items.query.all()
    else:
        items = Badyet_Items.query.filter_by(category=categry).all()

    return [
        {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'length': item.length,
            'amount': item.amount,
            'owner_id': item.owner_id
        } for item in items
    ]

def get_sum(categry=None):
    total = ""
    if categry == None or categry == "":
        total = db.session.query(func.sum(Badyet_Items.amount)).scalar()
    else:
        total = db.session.query(func.sum(Badyet_Items.amount)).filter_by(category=categry).scalar()

    return total