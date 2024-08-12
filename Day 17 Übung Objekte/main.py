#Quiz
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

    def report(self):
        print(self.id)
        print(self.username)
        print(self.followers)

    def followerup(self):
        self.followers += self.followers + 1

user_1 = User(12030123, "Nils")


user_1.report()
user_1.followerup()
user_1.report()