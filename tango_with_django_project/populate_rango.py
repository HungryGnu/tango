import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
#Important, setdefault before you import Django
import django
django.setup()
from rango.models import Category, Page


# When importing Django models make sure you import project settings
# By importing Django and setting the environment variable DJANGO_SETTINGS_MODULE
# to be you projects settings i.e. 'tang_with_django_project.settings'

# if you don't do this you will get an error when you try to import your models

def populate():
    # Create lists of dictionaries containing pages
    # Create a dictionary of dictionaries for categories
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 124},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 60},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views": 312}]
    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/q.0/intro/tutorial01/",
         "views": 45},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 67},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 112}]
    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views": 90},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views": 85}]

    cats = {"Python": {"pages": python_pages,
                       "views": 128,
                       "likes": 64},
            "Django": {"pages": django_pages,
                       "views": 64,
                       "likes": 32},
            "Other Frameworks": {"pages": other_pages,
                                 "views": 32,
                                 "likes": 16}
            }

    # IF you want to add more categories of pages,
    # add them ot the dictionaries above.
    # The code blow goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using python2.x then use cats.iteritems()
    # see http://docs.quantifiedcocde.com/python-anti-patters/readability/
    # for more information about how to iterate over dictionary properly

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    # print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    # get_or_create returns a tuple of (object, created) where object
    #  is a reference to the model instance and created is a boolean
    # that indicates if it had to be created.  [0] in the statement abouve returns only 'object'
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script ...")
    populate()
