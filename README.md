
equirements

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

## Views along with their payloads
```
def index(request):
GET request
This view responds to a get request at url ('/')
This function returns the paginated home page with 5 entries per page 
```
```
def article_detail(request,**kwargs):
GET request
This page returns with all the paragraps of a blog entry
url=('/article') payload= {'id' : some number}  id here is primary key for the blog post 
can be tested directly using get('/article/4') (just for example)
```
```
def show_comments(request,**kwargs):
GET request
This page returns all the comments on a paragraph of a blog entry.
url=('/article/show_comments/') payload={'id'= : primary key}  This id here is primary key of the paragrah .
```
```
def post_a_blog(request):
POST request
url=('/post_a_blog') payload={'title' : text, 'body' : text} 
Makes a new blog entry 
The function parses the body of the entry for paragraps and store them in the models defined.
redirects to the home page
```
```
def post_a_comment(request,**kwargs)
POST request
URL=('/article/post_a_comment') payload ={'id': primary_key_for_paragraph}
Make a new comment entry .
Redirects to the paragraph on which comment was made
```





