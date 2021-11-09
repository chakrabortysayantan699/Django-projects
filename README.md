## Django Notes 📚

1. First enter your enviourment (**For my case it's base (Anaconda) and install django**)
2. Now we can check the installation by **django-admin --version** it will show some version now We are ready to go🚀
3. For creating a project create a folder then in that folder run **django-admin startproject <project_name>**
   - the project folder will consist some necessary files 
       - manage.py(it will be useful to run our server)
       - Project_folder(urls.py,settings.py etc)
4. Now we have to create our app(one project can contain one or more apps)
   - run **django-admin startapp <app_name>**
   - this app also conatin (seetings.py and other file but urls.py missing for that)
   - we have to create an urls.py file for our app and should link views.py file in that
   - mandatorily connect project's urls.py with app's urls.py by **path('',include('app_name.urls'))**
   - **''** that specify it's a home directory    
5. Now we have to edit views.py for a different views  
   - we can create a diiferent html file 
   - connect that file in views.py to show those thing and send that file as a HttpResponse
   - it can show the original view of that html
   - for every action we need to return a page or response otherwise it will throw an error
6. **Now the speacial power of django mixing of static📖+ dynamic💥 (with jinja)**
   - in **Vscode use Jinja and in sublime use jinja2 extention**
   - base jinja page will remain static for every page that we will extends on it 
   - {%block content%} you have to write {% endblock %}
   - for extending {%extends base.html%}
7. **DTL(django template language)**
   - We will get all inputs and show all outputs in website page so we need html page
   - that's why we need a **Template folder** in this we will store all the html files that we will use
   - and we need to change **settings.py of main project** 
   ```python
   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
   ]
   ```  
   - Now here we can store our html like the project shown here
8. **At this point we can see only our html file** but a single html page is simple🥱
   - For a great UI we need other filles like js,css,images,fonts etc....
   - all this files are static files
   - we need folder in which we can store all other necessary files 
   - and again we need to change **settings.py of main project** 
   ```python

   STATIC_URL = '/static/'
   STATICFILES_DIRS=[
      os.path.join('./static')
   ]
   STATIC_ROOT=os.path.join('BASE_DIR','assets')
   ```
   - now we have to run a command **python manage.py collectstatic** an if we get folder like assets **congratulation🍾** we are done with this this part
   - then in the html page we have to **{% load static %}** 
   - and we have to add **{%static %}** in every line where static files are used
   - like **<link href="{%static 'vendor/bootstrap/css/bootstrap.min.css' %}" rel="stylesheet" />**
   - now we can see a great UI with our all associate files

9. **Now our aim is to dynamically change content of without touch the code**
   - For this we need to go in some steps

|   **status**  |
|---------------|
|**In progress**|



