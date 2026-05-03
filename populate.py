import os
import django
from random import randint
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fakerproject.settings")
django.setup()


from fakerapp.models import Student


def generate_ph_no():
    d1 = randint(6, 9)
    num = "" + str(d1)
    for i in range(9):
        num += str(randint(0, 9))
    return int(num)


def populate(n):
    fake = Faker()
    for i in range(n):
        frollno = fake.random_int(min=1, max=999)
        fname = fake.name()
        fdob = fake.date()
        fmarks = fake.random_int(min=1, max=100)
        femail = fake.email()
        fphonenumber = generate_ph_no()
        faddress = fake.address()

        # Load All Fake Data in to Model(Student)

        Student.objects.get_or_create(
            rollno=frollno,
            name=fname,
            dob=fdob,
            marks=fmarks,
            email=femail,
            phonenumber=fphonenumber,
            address=faddress,
        )


n = int(input("Enter the number of records to be inserted: "))
populate(n)
print(f"{n} records inserted successfully")
