from ..models import Badyet_Items

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