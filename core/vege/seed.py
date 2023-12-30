from faker import Faker
fake = Faker()
import random
from .models import *

def seed_db(n=10) -> None:
# sourcery skip: remove-zero-from-range
    try:
        for _ in range(n):
            department_objs = Department.objects.all() #having multiple depts [1,2,3,4..], so generating random index for dept
            random_index = random.randint(0, len(department_objs)-1)
            department = department_objs[random_index]
            student_id = f'STU-0{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            #creating objects
            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )
    except Exception as e:  
        print(e)

# from faker import Faker
# import random
# from .models import *

# fake = Faker()

# def seed_db(n=10) -> None:
#     try:
#         # Ensure there are departments available
#         department_objs = Department.objects.all()

#         if not department_objs:
#             print("Error: No departments found.")
#             return

#         for _ in range(n):
#             department = random.choice(department_objs)

#             student_id = f'STU-0{random.randint(100, 999)}'
#             student_name = fake.name()
#             student_email = fake.email()
#             student_age = random.randint(20, 30)
#             student_address = fake.address()

#             student_id_obj = StudentID.objects.create(student_id=student_id)

#             student_obj = Student.objects.create(
#                 department=department,
#                 student_id=student_id_obj,
#                 student_name=student_name,
#                 student_email=student_email,
#                 student_age=student_age,
#                 student_address=student_address
#             )

#     except Exception as e:
#         print(e)

