x = lambda u: u.is_authenticated

class user():
    def is_authenticated(self):
        print("au yes")
u = user()
x(u)()