# todoapp
Flask todo application with CRED operation, Swagger UI, Docker, Docker Swarm &amp; Restplus APIs


## What is this repository for? ###

* Quick learning of Flask based project
* Version control
* Getting start with Flask
* [Todoapp] - (https://github.com/rmehra7/todoapp)


## How do I get set up? ###

### [Without #Docker]

* Setup virtualenv - *python3 -m venv env*
* Install dependencies
* Do the server configuration
* Database configuration - (Note - In this app using file based database)


### How to run tests

* Export the env file - **.env.test**
* Command to run test cases - **pytest tests/*** from root dir


### Code coverage report

* Genearte code coverage report - **coverage run --source='./src'  -m pytest tests/***
* For stdout report [RUN] - *coverage report -m*
* For HTML report [RUN] - *coverage html*

### [With #Docker]

* Create a docker image - *docker build . -t image-name:image-tag*
* Init your docker swarm 
* Do the required configration in docker service file
* Deploy docker service

## For contribution

* Code review
* test cases
* Other suggesstions to optimize code

## Contact info

* admin - *rmehra9292@gmail.com*


## Author

* Rahul Mehra (rmehra9292@gmail.com)

    