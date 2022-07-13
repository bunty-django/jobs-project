from datetime import date
import email
import os
from turtle import title

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usjobportal.settings')
import django

django.setup()

from testApp.models import *
from faker import Faker
from random import *

fake = Faker()


def phonenumbergen():
    d1 = randint(7, 9)
    num = '' + str(d1)
    for i in range(9):
        num = num + str(randint(0, 9))
    return int(num)



def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('project manager', 'team lead', 'Software engineer'))
        feligibility = fake.random_element(elements=('MTECH', 'BTECH', 'MCA', 'Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphunenumber = phonenumbergen()
        hydjobs_record = hydjobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle,
                                                      eligibility=feligibility, address=faddress, email=femail,
                                                      phone_number=fphunenumber)


populate(25)
