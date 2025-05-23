from flask_blog import app, db
from flask_blog.models import User, Posts

with app.app_context():
    # Create all tables
    db.create_all()
    print("Database tables created.")

    users_data = [
        {'username': 'Tejashree Raul', 'email': 't@gmail.com', 'password': '123'},
        {'username': 'Gauri Pachling', 'email': 'g@gmail.com', 'password': '456'},
        {'username': 'Annanya Gali', 'email': 'a@gmail.com', 'password': '789'}
    ]

    # Loop through and add users if they don't already exist
    for data in users_data:
        if not User.query.filter_by(email=data['email']).first():
            user = User(username=data['username'], email=data['email'], password=data['password'])
            db.session.add(user)
            #print(f"Added user: {data['username']}")
        #else:
            #print(f"User {data['username']} already exists.")

    db.session.commit()
    print("All users committed to the database.")

    all_users= User.query.all()

    # print(User.query.first())

    # for u in all_users:
    #     print(u)

    # us= User.query.filter_by(username='Gauri Pachling').first()
    # print(us)

    user= User.query.get(1)
    print(user)
    post_1= Posts(title='Blog 1', content='First Post Content!', user_id= user.id)
    post_2= Posts(title='Blog 2', content='Second Post Content!', user_id= user.id)
    db.session.add(post_1)
    db.session.add(post_2)
    db.session.commit()

    pst = user.posts
    for post in user.posts:
        print(post)
        print(post.author)

    User.query.delete()
    user= User.query.get(1)
    print(user)
    db.create_all()
    db.session.commit()