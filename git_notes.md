# GitHub Workflow

When contributing to a codebase that is hosted on GitHub, one does not push changes directly to the main repository. Instead, you push your work to a `fork` of the `repository`, and then you request that your changes be pulled into the main repository by making a `pull request`.

Below are the steps required to make this happen. If you have already gone through these steps before and you want to make another contribution, skip to step 3.

1.	Fork the repository on GitHub by pressing the `Fork` button in the upper right of the main repository’s GitHub page. This creates a copy of the repository under your account.

2.	Clone your `fork` to your machine. Make sure you are on the page for your fork and **not** the page of the main repository. You can get the clone URL by clicking on the green `Clone or Download` button.

3.	cd into your cloned directory.

4.	Create a `new branch` to do your work in. This is not always required, but it is good practice for each pull request to come from a unique branch. If you want to make multiple distinct pull requests for a single repository, it is required that they each be in a separate branch, so you might as well get in this habit. When you clone the repository, you will have the main branch checked out. This branch is usually called `master`. Check to see what branch you currently have checked out by running git branch. This will show you all of the branches that currently exist in your local repository, and the one that is checked out will be marked with an asterisk. You can always switch back to the master branch by running `git checkout master`. Create a new branch and check it out simultaneously using the following command. Name your branch something appropriate for the work you are about to do:`git checkout -b branch_name`. Any work that you commit will be committed to the currently checked out branch.

5.	Do your work.

6.	`Add` your changes with `git add <filename>` or `git add -A` to add all changes.

7. 	`commit` your changes with `git commit -m "commit message goes here"`

8.	`Push` your changes to your fork by running the following command (where `branch_name` is the name of the branch you just committed to): `git push origin branch_name`. If the branch does not yet exist in your fork on GitHub, it will be created automatically when you first push to it. The name `origin` refers name of the remote repository that you cloned from. In the last step of this guide you will create a link to a second remote repository.

9.	Create a `pull request`. On the GitHub page for your `fork` you should see a new message that you have pushed to a branch, and a `Compare & pull request` button. Click on this button, make sure everything looks good, and click on `Create pull request`. The owner(s) of the repository can now review your pull request, and merge your changes if they look good.

10.	Once your changes have been accepted, or if the main repository has changed, you will want to update your local repository’s master branch to reflect the new masterbranch of the main repository. If this is the first time you are doing this, you need to add a `new remote`, which links your local repository with a remote repository. Cloning automatically created the remote named origin, you can create a remote that points to the main repository like so: `git remote add main <url of the main repository>` You can get the URL for the main repository using the `Clone or download` button on the page of the main repository. Now switch back to the master branch in your local repository by running `git checkout master`. Pull in the latest version of the main repository’s master branch by running `git pull main master`. If all goes well, your local master branch will now be the same as the main repsitory’s master branch. To make another contribution, go back to step 4.


____
## Note:
Look at [this](https://help.github.com/en/articles/connecting-to-github-with-ssh) to learn how to use `ssh` while commiting so that you do not have to put in your github password everytime you use git.
