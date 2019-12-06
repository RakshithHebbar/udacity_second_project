from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user1 = User(
    name='Rakshith',
    email='rakshithvs246@gmail.com',
    picture=''
)


session.add(user1)
session.commit()

category_json = json.loads("""{"all_categories": [
    {
        'name' : 'Snowboarding',
        'user': user1
    },
    {
        'name': 'Basketball',
        'user': user1
    },
    {
        'name': 'Foosball',
        'user': user1
    },
    {
        'name': 'Baseball',
        'user': user1
    },
    {
        'name': 'Frisbee',
        'user': user1
    },
    {
        'name': 'Soccer',
        'user': user1
    }
]}""")


for e in category_json['all_categories']:
category_input = Category(
name=str(e['name']),   
user_id=e['user']
)
session.add(category_input)
session.commit()

item1 = Item(
    name='Snowboard',
    description='Best way for any terrain and condition',
    category=category1,
    user=user1
)

item2 = Item(
    name='Goggles',
    description='Best way for any terrain and condition',
    category=category1,
    user=user1
)

session.add(item1)
session.add(item2)

session.commit()

print('Finished populating the database!')
