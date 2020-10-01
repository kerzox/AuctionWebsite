class Item:
    def __init__(self, name, description, image, currency):
        self.name = name
        self.description = description
        self.image = image
        self.currency = currency
        self.comments = list()
    
    def set_comments(self, comment):
        self.comments.append(comment)


class Comment:
    def __init__(self, user, text, created_at):
        self.user = user
        self.text = text
        self.created_at = created_at

class Login:
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd