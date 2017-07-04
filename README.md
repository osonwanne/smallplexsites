# Smallplex
Smallplex - Shares and Investor landing page, with links/redirects to separate web apps. http://smallplex.com

[![Smallplex Properties](https://s3-us-west-2.amazonaws.com/smallplex/SmallplexSites.PNG "Websites")](http://smallplex.com)

**Set-up and installation:**

1. git clone https://github.com/osonwanne/smallplexsites.git

2. cd smallplexsites

3. pip install -r requirements.txt

(Optional - resolves ImportErrors on Ubuntu)
* sudo easy_install django-treebeard 
* sudo apt-get install python-unicodecsv
* sudo pip install glue

4. python manage.py migrate

5. python manage.py collectstatic

6. python manage.py runserver

* Update Settings for Sendgrid credentials