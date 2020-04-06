import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','GT.settings')

import django
django.setup()

##Fake Pop Script

import random
from GT_app.models import AccessRecord,Webpage,Topic
from faker import Faker


fakegen = Faker()
topics= ['Search','Social','MarketPlace', 'News', 'Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # Getting the topic for each entry
        top = add_topic()

        #Createing Fake Data for that entry
        fake_url= fakegen.url()
        fake_date=fakegen.date()
        fake_name= fakegen.company()


        #Creating the new Webpage(name, bases, dict) entry

        wepge = Webpage.objects.get_or_create(topic=top, url = fake_url, name= fake_name)[0]


        #Creating fake AccessRecord(name, bases, dict) for that page


        acc_rec = AccessRecord.objects.get_or_create(name= wepge, date=fake_date)[0]


if __name__ == '__main__':
    print(" poupulating script")
    populate(1)
    print(" Populating complete")
