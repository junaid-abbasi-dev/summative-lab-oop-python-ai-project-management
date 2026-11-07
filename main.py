import argparse
from models.user import User
from services.storage_service import StorageService

parser = argparse.ArgumentParser(description="Project management CLI")
subparsers = parser.add_subparsers(dest="command")

add_user = subparsers.add_parser("add-user")
add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)

args = parser.parse_args()

if args.command == "add-user":
    storage = StorageService()
    data = storage.load()
    user = User(args.name, args.email)
    data["users"].append(user.to_dict())
    storage.save(data)
    print(f"Added user {user.name}")