# Contributing to Gajabaar writeups-2020

<p>When contributing to this repository, please follow the below described <b>Workflow for writeups</b> and the <b>Standards</b> for the changes that you would like to integrate.
</p>

## Workflow for writeups
<ol>
  <li><b>Fork Repository: </b>To fork the <i>writeups-2020</i> repository, click on the <b>Fork</b> button on the top rightmost side of the repository.</li>
  <li><b>Clone the forked repository: </b>Clone the repository to your local computer. You can use command <code>git clone link_of_forked_repository</code></li>
  <li><b>Add remote (original repo): </b>Add Gajabaar/writeups-2020 as remote repository. Use command <code>git remote add remote_name link_of_Gajabaar_repo</code></li>
  <li><b>Fetch changes from original repo: </b>Fetch changes from Gajabaar/writeups-2020. Use command <code>git fetch remote_name</code></li>
  <li><b>Create a topic branch: </b>To add your changes create a topic branch. You can use <code>git checkout -b branch_name</code> to checkout to the topic branch</li>
  <li><b>Add your changes locally to the topic branch: </b>Make changes that you like locally. Stage and commit your changes.</li>
  <li><b>Push your branch changes on your forked repository: </b>After you have committed your changes, push them to your forked repository. Use command <code>git push origin branch_name</code></li>
  <li><b>Create Pull Request from the branch: </b>Go to your forked repository. Under your topic branch_name notice a button <b>Pull Request</b>. Click the button to make a pull request. Give a descriptive title and description.</li>
  <li><b>After your request gets accepted: </b></li>
  <ol>
    <li>Delete topic branch locally and in github. To delete the branch locally, use command <code>git branch -d branch_name</code>. To delete the branch on your remote forked repository, use command <code>git push origin --delete branch_name</code></li>
    <li>Sync forked repository and local repository. To sync with Gajabaar/writeups-2020, fetch the changes from remote_name. Merge those changes locally and push them to your forked repository.</li>
  </ol>
  <li><b>Repeat from step 4 for new changes.</b></li>
</ol>

## Writeup Standards
<ul>
  <li>Use welcoming and inclusive language</li>
  <li>Be respectful of differing viewpoints and experiences</li>
  <li>Trolling, insulting/derogatory comments, and personal or political attacks will not be considered</li>
  <li>Do not publish others' private information, such as a physical or electronic address, without explicit permission</li>
  <li>Do not commit unnecessary errors like whitespace changes that annoys the team</li>
  <li>Use short and descriptive commit messages to ease the understanding on any commit.</li>
  <li>Make your changes in relevant branches. Do not use master branch for all the writeups, instead create a topic branch with relevant branch name</li>
  <li>Do not commit many changes at once. Commit on each logically separate changeset</li>
  <li>While making a pull request, target to the <b>master</b> branch</li>
  <li>Specify a descriptive title to make searching for the pull request easier</li>
  <li>Place detail description during the pull request</li>
  <li>Do not add a lot of things in one pull request</li>
</ul>
  
<p>
  Thank you for taking the few moments to read this far! You're already way ahead of the curve, so keep it up!
</p>
