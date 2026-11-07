class Project:
    def __init__(self, user, title, description, due_date):
        self.user = user
        self.title = title
        self.description = description
        self.due_date = due_date

    def to_dict(self):
        return {
            "user": self.user,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["user"], data["title"], data["description"], data["due_date"])