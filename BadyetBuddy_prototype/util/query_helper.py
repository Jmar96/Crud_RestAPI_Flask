from ..app.models import Badyet_Items

def get_items(categry):
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