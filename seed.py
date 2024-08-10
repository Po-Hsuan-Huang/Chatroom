import random
from app import db, Message, User, app  # Import the app from your main file

def seed_data():
    # List of available profile photos
    profile_photos = [
        "static/images/11.png",
        "static/images/16.png",
        "static/images/17.png",
        "static/images/18.png",
        "static/images/19.png",
        "static/images/20.png",
        "static/images/21.png",
        "static/images/22.png",
        "static/images/23.png",
        "static/images/24.png",
        "static/images/26.png",
        "static/images/27.png",

    ]

    # Create some sample users with randomly selected profile photos
    users = [
        {"username": "alice", "password": "password1"},
        {"username": "bob", "password": "password2"},
        {"username": "charlie", "password": "password3"},
        {"username": "david", "password": "password4"},
        {"username": "eve", "password": "password5"}
    ]

    used_photos = set()

    # Add the users to the session
    for user_data in users:
        available_photos = [photo for photo in profile_photos if photo not in used_photos]
        profile_photo = random.choice(available_photos)
        used_photos.add(profile_photo)
        user = User(username=user_data["username"], profile_photo=profile_photo)
        user.set_password(user_data["password"])
        db.session.add(user)

    # Create some sample messages
    messages = [
        Message(content="Hello, world!", sender="alice"),
        Message(content="How are you?", sender="bob"),
        Message(content="This is a test message.", sender="charlie"),
        Message(content="Welcome to the chatroom.", sender="david"),
        Message(content="Let's chat!", sender="eve")
    ]

    # Add the messages to the session
    db.session.bulk_save_objects(messages)
    
    # Commit the session
    db.session.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    with app.app_context():  # This ensures that we're working inside the Flask application context
        db.create_all()       # Create the tables
        seed_data()           # Seed the data