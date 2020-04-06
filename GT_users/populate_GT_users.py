import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','GT_users.settings')

import django
django.setup()

##Fake Pop Script

import random
from user_app.models import User
from faker import Faker


fakegen = Faker()



def populate(N=5):
    for entry in range(N):



        #Createing Fake Data for that entry

        fake_name= fakegen.name().split()
        fake_name_first = fake_name[0]
        fake_name_last = fake_name[1]

        fake_email = fakegen.email()



        #Creating the new User(name, bases, dict) entry

        user = User.objects.get_or_create(first_name = fake_name_first,last_name = fake_name_last, emails= fake_email)






if __name__ == '__main__':
    print(" poupulating script")
    populate(10)
    print(" Populating complete")
