# MyImageCollection

In this website you can find Images with best quality based on diffrent categories which is developed in Django with mysqlite as Database and HTML,CSS ,JS along Bootstrap Framework in Frontend gives an amazing learning as well as handling experience.  

Some of the steps which are important during the project:
1.How to handle request in Pycharm? - Client-Server Architecture

     Browser - Client
     http://127.0.0.1:8000/ - Server is running at that port

2. When we create a new app(myapp) there is a file models.py which is used to handle to database.

==> Model --> is a entity that store data.

==>CASCADE -->Means when we delete 'Category' then all the images related to it get deleted.

3. Sync it(Model) with Db i.e we want tables in the DB of Category for that we add our 'myapp' with 'settings' by setting of imagebazar -->INSTALLED_APPS

4. In admin.py we have to register our both model which is Category and Image by running following command.
	admin.site.register(model_name)

5. Make admin panel by creating Username and password by runnibg following command:
    python manage.py create superuser
    add name
    add email

6. To change the 'Category object' in django-admin to it's title add func. in models.py def__str__(self):
			   return self.title
to show the title of Category.

7.Now we have to create a directory 'media' to upload our categories photos.
And make some changes in settings.py by adding MEDIA_URL='/media/'(to access photos we start from '/media/') and 
MEDIA_ROOT i.e path.And finally some changes in url.py which is static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

8. Add Categories and images in Django Admin .

9. Now add navbar in home.html using {%include'navbar.html' %}using Bootstrap.

10. After laying the structure of the home.html page we have to load all the images in the views page using Image.objects.all() and pass it using show_home_page.html
