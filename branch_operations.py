# branch_operations.py
import os

def create_branch():
    branch_name = input("Enter new branch name: ")
    os.system(f"git checkout -b {branch_name}")

def switch_branch():
    branch_name = input("Enter branch name to switch to: ")
    os.system(f"git checkout {branch_name}")

def list_branches():
    os.system("git branch -a")

def merge_branch():
    current_branch = os.popen("git branch --show-current").read().strip()
    branch_to_merge = input(f"Enter the branch name you want to merge into {current_branch}: ")
    os.system(f"git merge {branch_to_merge}")

def delete_branch():
    branch_name = input("Enter the branch name to delete: ")
    local_delete = input("Delete locally? (y/n): ").lower() == 'y'
    remote_delete = input("Delete remotely? (y/n): ").lower() == 'y'
    
    if local_delete:
        os.system(f"git branch -d {branch_name}")
    if remote_delete:
        os.system(f"git push origin --delete {branch_name}")
