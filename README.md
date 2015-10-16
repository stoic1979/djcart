# djCart
djCart is a simple shopping cart developed in django

Under R&D by weavebytes.


Features
--------

* Add categories for items
* Add items in different categories

Unit Tests
--------

* Run tests as:-
 $ python manage.py test --keepdb

Setup Instructions
--------

* grappelli - for admin skinning

 - pip install django-grappelli

 - Open settings.py and add grappelli to your INSTALLED_APPS (before django.contrib.admin):

    INSTALLED_APPS = (
        'grappelli',
        'django.contrib.admin',
    )

 - For more details, follow grappelli docs:-
    http://django-grappelli.readthedocs.org/en/latest/quickstart.html#installation

$ python manage.py collectstatic

* simple captcha

 - You must install following dependencies:-
    apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev

 - Then installing simple catcha with:-
    pip install Pillow
    pip install django-simple-captcha

 - For more details, follow simple captcha docs:-
   http://django-simple-captcha.readthedocs.org/en/latest/usage.html
