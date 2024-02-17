### Django deployment using _Docker-compose_ and _AWS_ 

*********

#### services used in this project:
* Docker
    + Creating an image for our app and run the services using docker-compose

* Django 
    + configurin a django app to configure and interact with our database (in this case **postgresql** ) and reverse proxy ( in this specific case **NGINX** )

* NGINX
  + used as reverse proxy to map our media and static urls to the right volume and other urls to uWSGI service

* Postgresql
  * run postgresql image as container to depends on our main django app container
  * configure Postgresql as the default database engine and interact with it through app container using docker-compose
  
#### some of the key features of this simulation

- [x] as our main django app service `depends-on` postgresql database service , we are implementing a `wait_for_db` command to check whether the database is ready or not before running our django app service

- [x] as we are simulating production ready terms, it's better to set _environment variable_ in our main django app and fed those variables from our _docker-compoes_ file while running our services where we have access to any other services such as <span style='color:
#87cefa'>Nginx, postgresql, ... </span>
    