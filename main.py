# main.py
from identity import check_git_identity, set_git_identity
from repo_operations import (initialize_repo, view_history, stash_changes, apply_stashed, repo_status,
                             clone_repo, pull_with_rebase, fetch_changes, add_remote, list_remotes, 
                             remove_remote, add_submodule, init_submodules, update_submodules)
from branch_operations import create_branch, switch_branch

def help_guide():
    print("""
    GitHub Repository Controller Help Guide:

    1. Initialize new repo:
    Initializes a new Git repository in the current directory, adds all files, commits them, and then pushes them to the provided GitHub repository link.

    2. Set Identity:
    Configure your Git user identity for either global (used across all repositories) or local (used just in the current repository) scope.

    3. Update Repository:
    Pulls latest changes, adds all changes, commits them with the provided message, and pushes them to the master branch of the remote repository.

    4. Create Branch:
    Creates a new branch in the Git repository with the given name.

    5. Switch Branch:
    Switches to the specified branch in the Git repository.

    6. View History:
    Displays the commit history log of the Git repository.

    7. Stash Changes:
    Temporarily saves changes that haven't been committed yet, allowing you to switch branches or perform other actions without committing.

    8. Apply Stashed Changes:
    Applies the changes you've previously stashed.

    9. Repository Status:
    Displays the current state of the repository, including any untracked, modified, or staged files.

    10. Exit:
    Exits the GitHub Repository Controller.

    Simply type the corresponding number for the desired action when prompted by the program.
    """)

def main():
    while True:
        print("GitHub Repository Controller")
        print("1. Initialize new repo")
        print("2. Set Identity")
        print("3. Update Repository")
        print("4. Create Branch")
        print("5. Switch Branch")
        print("6. View History")
        print("7. Stash Changes")
        print("8. Apply Stashed Changes")
        print("9. Repository Status")
        print("11. Help")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            initialize_repo()
        elif choice == '2':
            scope = input("Set identity for 1. Global or 2. Local: ")
            set_scope = 'global' if scope == '1' else ''
            set_git_identity(set_scope)
        elif choice == '3':
            commit_message = input("Enter the commit message: ")
            os.system("git pull")
            os.system("git add .")
            os.system(f'git commit -m "{commit_message}"')
            os.system("git push origin master")
        elif choice == '4':
            create_branch()
        elif choice == '5':
            switch_branch()
        elif choice == '6':
            view_history()
        elif choice == '7':
            stash_changes()
        elif choice == '8':
            apply_stashed()
        elif choice == '9':
            repo_status()
        elif choice == '11':
            help_guide()
        elif choice == '12':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
