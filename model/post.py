from model.user import User


class Post:
    def __int__(self, id, body: str, author: User):
        self.id = id
        self.body = body
        self.author = author
    def JSON(self):
        return {'id': self.id, 'body': self.body, 'author': self.author}
