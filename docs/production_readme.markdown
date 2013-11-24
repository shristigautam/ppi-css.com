static IP = 162.222.181.45

## Update the Instance ##
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install git

sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install virtualenv

## Install Numpy and Scipy (SciPy requires Fortran compiler) ##
sudo apt-get install gfortran

sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

sudo pip install prody


## Install the Web Server (Apache2) ##
This is a very basic tutorial that doesn't get into the details of configuring the address
https://developers.google.com/compute/docs/quickstart

Understanding the apache2 configuration files is important for getting this to work correctly and it would appear that Debian does things a bit non-standard.  See here for more details:

http://www.control-escape.com/web/configuring-apache2-debian.html


sudo apt-get install apache2 libapache2-mod-wsgi

By default, the following page is served by the install:

    /usr/share/apache2/default-site/index.html

Now we need to update the virtual hosts settings on the server.  For Debian, this is here:
/etc/apache2/sites-enabled/000-default 


Restart the service

    sudo service apache2 restart 

ERROR MESSAGES:
[....] Restarting web server: apache2apache2: apr_sockaddr_info_get() failed for (none)
apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.0.1 for ServerName
 ... waiting apache2: apr_sockaddr_info_get() failed for (none)
apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.0.1 for ServerName
. ok 
Setting up ssl-cert (1.0.32) ...
hostname: Name or service not known

### Need to do Configuration Work ###

sudo vi /etc/apache2/sites-available/default
plus edit the wsgi.py file

http://thecodeship.com/deployment/deploy-django-apache-virtualenv-and-mod_wsgi/




## Install and Configure the Database (MySQL) ##

sudo apt-get install mysql-server
- create a root password

mysql_secure_installation
- type in your password and then answer all questions "Y"

sudo apt-get install python-mysqldb

mysql --user=root --password=INSERT PASSWORD
mysql> create database django_test;
mysql> quit;


## Grab the Django App from GitHub

git clone https://github.com/murphsp1/myproject.git

edit the settings to reflect new database


WHERE wsgi.py is
/home/seanmurphy/myproject/myproject/myproject

WHERE STATIC IS:
/home/seanmurphy/myproject/myproject/myproject/myapp/static


http://192.158.29.226/myapp/init_table_data_load/

but need to update the original source to have a proper path

From the command line in the directory with "manage.py" type:

    python manage.py syncdb
    python manage.py migrate






You need to do two things

In the Amazon Web Service admin panel, create an elastic IP in the same region as your instance and associate that IP with your that instance (IPs cost nothing while they are associated with an instance, but do cost if not).
Add a A record to the DNS record of your domain mapping the domain to the elastic IP address assigned in (1). 

Your domain provide should either give you some way to set the A record (the IP address), or it will give you a way to edit the nameservers of your domain.








#need to remove scipy and numpy from requirements file
#otherwise they really don't seem to install properly
#also, must install psycopg2 separately

sudo apt-get install python-virtualenv


sudo pip install -r ./requirements.txt 






#need to setup appache webserver


/home/seanmurphy/myproject/myproject/myproject

## GCE - Only Need to Do 
#need to configure GCE firewall settings
gcutil addfirewall http2 --description="Incoming http allowed." --allowed="tcp:http" --project="1040981951502"




references:
http://thecodeship.com/deployment/deploy-django-apache-virtualenv-and-mod_wsgi/


The Django Book
Deploying Django
http://www.djangobook.com/en/2.0/chapter12.html



Complete Single Server Django Stack Tutorial
http://www.apreche.net/complete-single-server-django-stack-tutorial/

START TO FINISH - SERVING DJANGO WITH UWSGI/NGINX ON EC2
http://adambard.com/blog/start-to-finish-serving-mysql-backed-django-w/

Non-techie Guide to setting up Django, Apache, MySQL on Amazon EC2
http://pragmaticstartup.wordpress.com/2011/04/02/non-techie-guide-to-setting-up-django-apache-mysql-on-amazon-ec2/

Deploying Django on Amazon EC2 Server
http://nickpolet.com/blog/1/

Deploying Python, Django on ec2 linux instance
http://blog.hguochen.com/blog/2013/09/deploying-python-django-on-ec2-linux-instance/

How to use Django with Apache and mod_wsgi
https://docs.djangoproject.com/en/1.4/howto/deployment/wsgi/modwsgi/


Setting up Django with Nginx, Gunicorn, virtualenv, supervisor and PostgreSQL
http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/


#need to install postgres ...
sudo apt-get install postgresql
sudo apt-get install libpq-dev
sudo pip install psycopg2

#need to setup postgres db and accounts
sudo passwd postgres   #update postgres user passwrd

seanmurphy@(none):~/myproject/myproject/myproject$ sudo su - postgres
sudo: unable to resolve host (none)
postgres@(none):~$ createdb test

postgres@(none):~$ createuser -P
Enter name of role to add: hello_django
Enter password for new role: 
Enter it again: 
Shall the new role be a superuser? (y/n) n
Shall the new role be allowed to create databases? (y/n) n
Shall the new role be allowed to create more new roles? (y/n) n

vi /etc/postgresql/9.1/main/pg_hba.conf





# New Debug 'cause server ain't working

Is server running?
sudo service apache2 status

What do the apache error logs say?
cat /var/log/apache2/error.log

gcutil --project="1040981951502" pull test2 /home/seanmurphy/myproject.tar.gz ./

gcutil --service_version="v1beta16" --project="1040981951502" ssh  --zone="europe-west1-a" "test2"


# Every Deployment

need to restart apache2
	
	sudo service apache2 restart
	
	./manage.py schemamigration css0 --auto
	./manage.py migrate css0   


log in and drop the table in the database

	mysql -u root -pPASSWORD -h HOSTNAMEORIP django_test

	drop table _______;
css0_scores

need to give permission to write to the directory for the user that will be writing files

drwxrwxrwx 2 seanmurphy seanmurphy   4096 Nov 20 18:51 .

drwxr-xr-x 3 seanmurphy seanmurphy   4096 Nov 20 15:35 ..

-rw-r--r-- 1 **www-data   www-data   136748 Nov 20 18:51 1FC2.pdb**

-rw-r--r-- 1 seanmurphy seanmurphy   6148 Nov 20 15:35 .DS_Store


Things to fix. Deployments generally suck. Something always breaks. 

Initial table data load is NOT working ... which is really odd.