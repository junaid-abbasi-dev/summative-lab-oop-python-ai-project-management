import argparse
from models.user import User
from services.storage_service import StorageService
from models.project import Project
from models.task import Task
from services.ai_client import OllamaClient

parser = argparse.ArgumentParser(description="Project management CLI")
subparsers = parser.add_subparsers(dest="command")

add_user = subparsers.add_parser("add-user")
add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)

list_users = subparsers.add_parser("list-users")

add_project = subparsers.add_parser("add-project")
add_project.add_argument("--user", required=True)
add_project.add_argument("--title", required=True)
add_project.add_argument("--description", required=True)
add_project.add_argument("--due-date", required=True)

list_projects = subparsers.add_parser("list-projects")
list_projects.add_argument("--user", required=True)

add_task = subparsers.add_parser("add-task")
add_task.add_argument("--project", required=True)
add_task.add_argument("--title", required=True)
add_task.add_argument("--assigned-to", required=True)

complete_task = subparsers.add_parser("complete-task")
complete_task.add_argument("--project", required=True)
complete_task.add_argument("--task", required=True)

summarize_project = subparsers.add_parser("summarize-project")
summarize_project.add_argument("--project", required=True)

args = parser.parse_args()

if args.command == "add-user":
    storage = StorageService()
    data = storage.load()
    user = User(args.name, args.email)
    data["users"].append(user.to_dict())
    storage.save(data)
    print(f"Added user {user.name}")

if args.command == "list-users":
    storage = StorageService()
    data = storage.load()
    for user_data in data["users"]:
        user = User.from_dict(user_data)
        print(f"{user.name} - {user.email}")

if args.command == "add-project":
    storage = StorageService()
    data = storage.load()
    project = Project(args.user, args.title, args.description, args.due_date)
    data["projects"].append(project.to_dict())
    storage.save(data)
    print(f"Added project {project.title}")

if args.command == "list-projects":
    storage = StorageService()
    data = storage.load()
    for project_data in data["projects"]:
        project = Project.from_dict(project_data)
        if project.user == args.user:
            print(f"{project.title} - {project.description} - due {project.due_date}")

if args.command == "add-task":
    storage = StorageService()
    data = storage.load()
    task = Task(args.project, args.title, "open", args.assigned_to)
    data["tasks"].append(task.to_dict())
    storage.save(data)
    print(f"Added task {task.title}")

if args.command == "complete-task":
    storage = StorageService()
    data = storage.load()
    updated_tasks = []
    found = False
    for task_data in data["tasks"]:
        task = Task.from_dict(task_data)
        if task.project == args.project and task.title == args.task:
            task.status = "complete"
            found = True
        updated_tasks.append(task.to_dict())
    data["tasks"] = updated_tasks
    storage.save(data)
    if found:
        print(f"Completed task {args.task}")
    else:
        print("Task not found")

if args.command == "summarize-project":
    storage = StorageService()
    data = storage.load()
    project = None
    for project_data in data["projects"]:
        candidate = Project.from_dict(project_data)
        if candidate.title == args.project:
            project = candidate
    if project is None:
        print("Project not found")
    else:
        tasks = []
        for task_data in data["tasks"]:
            task = Task.from_dict(task_data)
            if task.project == project.title:
                tasks.append(task)
        client = OllamaClient()
        print(client.summarize_project(project, tasks))