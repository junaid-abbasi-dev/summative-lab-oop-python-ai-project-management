class Task:
    def __init__(self, project, title, status, assigned_to):
        self.project = project
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    def to_dict(self):
        return {
            "project": self.project,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["project"], data["title"], data["status"], data["assigned_to"])