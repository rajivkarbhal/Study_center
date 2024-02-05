from git import Repo
from git import GitCommandError
import re

def git_commit_and_push(repository_path, commit_message):
    
    repo = Repo(repository_path)
    
    try:
        repo.git.add('.')

        repo.git.commit('-m', commit_message)

        if not repo.active_branch.tracking_branch():
            upstream_branch = f'origin/{repo.active_branch.name}'
            repo.git.branch('--set-upstream-to', upstream_branch)

        origin = repo.remote(name='origin')
        origin.push()

        print("Changes committed and pushed successfully.")

    except GitCommandError as e:
        print(f"Error: {e}")


print("********** Mentioning the name and modifications are mandatory. **********")

repository_path = 'C:/GitHub_Demo/Study_center'

prnm = input("Enter your name: ")
chn = input("Describe changes done (Modification, Addition, Deletion etc.): ")

commit_message = prnm + ":" + "\t" + chn

if (pat := re.match(r".+:\t.+", str(commit_message), re.IGNORECASE)):
    git_commit_and_push(repository_path, commit_message)

else:
    print ("Change/s are not updated to GitHub:  Please ensure that the name and modifications are properly mentioned.")