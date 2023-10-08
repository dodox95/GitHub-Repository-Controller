# GitHub Repository Controller

The GitHub Repository Controller is a command-line interface (CLI) tool designed to simplify the most common git operations. By using this controller, you can perform various Git tasks without having to remember each individual Git command. From initializing new repositories to managing branches, this tool covers a range of essential Git functionalities.

## Features:
1. **Initialize New Repository**: Quickly set up a new repo and push it to GitHub.
2. **Set Identity**: Define your Git user identity either globally or for the current repository.
3. **Update Repository**: Pull the latest changes, commit your work, and push to the master branch.
4. **Branch Management**: Create, switch, and manage branches seamlessly.
5. **View Commit History**: Display the entire commit log of your repository.
6. **Stash Management**: Stash your changes temporarily and apply them later.
7. **Repository Status**: See the current state, including untracked or modified files.
8. **Clone Repositories**: Easily clone other repositories into your local environment.
9. **Remote Management**: Add, list, or remove remote repositories.
10. **Submodules**: Add, initialize, and update submodules with ease.

## Usage:
Upon running the program, you will be presented with a list of available operations. Choose the desired operation by entering its corresponding number.

To access the help guide at any point, select the 'Help' option from the menu.

## Development:
This tool is split into different Python modules to maintain modularity:

- **main.py**: The main driver of the application, containing the primary menu and the user interaction loop.
- **repo_operations.py**: Holds functions related to repository operations like initialization, cloning, and status checking.
- **branch_operations.py**: Contains functionalities related to branch management.
- **identity.py**: Manages user identity settings on Git.

## Contribution:
Feel free to fork this project and submit pull requests for any enhancements or fixes. Your contributions are welcome!

## License:
This project is open-source and available under the [MIT License](LICENSE.md).

