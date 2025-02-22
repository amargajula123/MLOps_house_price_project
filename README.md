# MLOps_house_price_project

## Start Machine Learning project.

### Software and account Requirement

this is my ML project regarding to the All hypothetical Algorithems and alrgm project


Application url:
[HousingPredictor](https://ml-regression-app.herokuapp.com/)
.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.9 -y
```

for windows use this 
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To clear the terminal screen 
```
cls
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To know the branch name 
```
git branch
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = amar.g982858@gmail.com
2. HEROKU_API_KEY = HRKU-5039c543-603d-42de-aea6-9065cf274f5e
3. HEROKU_APP_NAME = ml-regression-app2

To stop app

```
heroku ps:scale web=0 --app <app name>
```

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```

gunicorn :=  #gunicorn which is used to run  flask 
          # application its basically designed for Linex based system 

```
python setup.py install
```


Install ipykernel for jupyter notebook

```
pip install ipykernel
```


Data Drift:
When your "Datset" statistics gets change we call it as data drift

what we do in Data_draft ?

Ans:-
we try to check the statistics of one dataset with the another dataset if the
statistics of both dataset "are SAME" there is 0 "Data_drift".
if the statistics of both dataset "are NOT SAME" there will be "Data_drift".
bassically we  compare statistics of both datasets





## Write a function to get training file path from artifact dir
#hi