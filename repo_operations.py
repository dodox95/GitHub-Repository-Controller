# repo_operations.py
import os

def initialize_repo():
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'initial commit'")
    repo_link = input("Enter the link to your GitHub repository: ")
    os.system(f"git remote add origin {repo_link}")
    os.system("git push origin master")

def view_history():
    os.system("git log")

def stash_changes():
    os.system("git stash")

def apply_stashed():
    os.system("git stash apply")

def repo_status():
    os.system("git status")

def clone_repo():
    repo_link = input("Enter the link of the GitHub repository to clone: ")
    os.system(f"git clone {repo_link}")

def pull_with_rebase():
    os.system("git pull --rebase")

def fetch_changes():
    os.system("git fetch")

def add_remote():
    remote_name = input("Enter a name for the remote (usually 'origin' for the main repo): ")
    remote_link = input("Enter the link of the remote repository: ")
    os.system(f"git remote add {remote_name} {remote_link}")

def list_remotes():
    os.system("git remote -v")

def remove_remote():
    remote_name = input("Enter the name of the remote to remove: ")
    os.system(f"git remote remove {remote_name}")

def add_submodule():
    submodule_repo = input("Enter the repository link of the submodule: ")
    submodule_path = input("Enter the path where you want to place the submodule (relative to the repo root): ")
    os.system(f"git submodule add {submodule_repo} {submodule_path}")

def init_submodules():
    os.system("git submodule init")

def update_submodules():
    os.system("git submodule update")