
# Requirements

You need python set up tools installed globally.

```
$ sudo apt-get install python-setuptools
$ pip install virtualenv
```

After that run these commands
```sh
$ git clone https://github.com/mukulpriya/Task_Repo.git
$ cd Task_Repo
$ virtualenv myenv
$ source myenv/bin/activate
$ pip install django==1.9
$ cd my_task
$ python manage.py makemigrations blog
$ python manage.py migrate 
$ python manage.py runserver
```
Your server is now up and running locally @
```
URL: localhost:8000 
```
 You will find nothing on the page beacuse the database is empty. To add a blog post
 type
 ```
URL: localhost:8000/post_a_blog 
  ```





   


