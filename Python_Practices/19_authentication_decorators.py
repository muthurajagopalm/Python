def requires_login(func):
    def wrapper(user):
        if not user.get("is_authenticated"):
            print("Access denied. Please login.")
            return
        return func(user)
    return wrapper

@requires_login
def view_dashboard(user):
    print(f"Welcome {user['username']} to your dashboard!")

user1 = {"username": "Alice", "is_authenticated": True}
user2 = {"username": "Bob", "is_authenticated": False}

view_dashboard(user1)  # Works
view_dashboard(user2) 
