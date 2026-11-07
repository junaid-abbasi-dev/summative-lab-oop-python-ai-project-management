def format_user(user):
    return f"{user.name} - {user.email}"

def format_project(project):
    return f"{project.title} - {project.description} - due {project.due_date}"