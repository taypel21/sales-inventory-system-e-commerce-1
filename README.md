# Sales-inventory-system-e-commerce
This is an e-commerce website developed for phase III of the reskill american bootcamp.
# Frontend
* Htmls5
* Css
* Vanilla Javascript
# Backend
* Python
* Django Framework
* postgresql database
# To work with this project
* Fork this repo.
* Clone this repo to your system.
* Switch to the develop branch
```
git checkout -b develop
```
* Set your github repo as the remote for your local git repo:
```
git remote add <unique_remote_name> <github_repo_url>.git
```
e.g
```
git remote add origin https://github.com/aayobam/sales-inventory-system-e-commerce.git
```
DO NOT ADD THE sales-inventory-system-e-commerce REPO AS YOUR REMOTE.
* Navigate to the relevant folder (e_commerce_frontend_backend)
* Do your work
* Stage the changed files you'll like to upload:
```
git add *
```
for all files. replace * with specific file names if you're only interested in those files.
* Commit to the develop branch with a clear, descriptive message and issue number, e.g.
```
git commit -m "Fixed models and bugs for customers as per issue #2."
```
* Push to the develop branch of the remote repo:
```
git push -u origin develop
```
* Do a pull request to the develop branch
# Installation instructions for backend
* Make sure you are in a virtual environment.
  - You can use the `virtualenv` package. If it's not installed on your local machine, install from your terminal, using
  ```
  pip install virtualenv
  ```
  - Once you have `virtualenv` on your machine, create a virtual environment with a name you choose:
  ```
  virtualenv <environment_name>
  ```
  - Next, activate the environment:
  For windows
  ```
  <environment_name>\Scripts\activate
  ```
  for linux(Ubuntu)
  ```
  source <environment_name>/bin/activate
  ```
