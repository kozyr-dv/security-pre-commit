# Gitleaks pre-commit hook

To effectively utilize the pre_commit_hook.py script in your Git project, follow these detailed instructions. They will help you set up and use a pre-commit hook that uses gitleaks to check your code for potential secrets before making a commit.

## Step 1: Installation of the Script

### 1. Download the script:

 - Save the pre_commit_hook.py script in the .git/hooks directory of your repository. You can do this by manually moving the file or using the following command:

```shell

mv pre_commit_hook.py your_repo_path/.git/hooks/

```
### 2. Make it executable:

- Execute the following command in your terminal while in the .git/hooks directory of your repository:

```shell

chmod +x pre_commit_hook.py

```
### 3. Rename for activation:

- To ensure the script runs as a pre-commit hook, rename the file or create a symbolic link:

```shell

ln -s pre_commit_hook.py pre-commit

```

## Step 2: Configuring 'git config'

To activate or deactivate the hook through git configuration:

### Activate the hook:

```shell

git config --bool hooks.gitleaks.enabled true

```

- Deactivate the hook:

```shell

git config --bool hooks.gitleaks.enabled false

```

This allows you to easily turn the gitleaks check on or off without having to delete or modify the hook.

# Step 3: Testing the Hook

To ensure that your hook is set up correctly and functioning:

- Make changes in your repository that might contain potential secrets.

- Try to commit:

```shell

  git commit -m "Test commit"

```

- Observe the outcome. If potential secrets are found, the hook will interrupt, display an appropriate message, and reject the commit.

# Step 4: Working with the Hook

- Check the settings:

To verify the activation status of the hook, use:

```shell

git config --get hooks.gitleaks.enabled

```
This will show whether the hook is enabled.

- In case of issues with 'gitleaks':

If you encounter problems with installing or running 'gitleaks', make sure that:


This approach allows you to maintain a high level of security by automatically detecting and preventing potential leaks before they are committed to your repository.






  



