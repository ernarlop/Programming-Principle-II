# Examples of using *args in Python functions.

def avg_GPA(*points) :
    sum = points[0] + points[1] + points[2] + points[3] + points[4]
    avg = sum / 5
    print ("The average GPA is: ", avg)
avg_GPA(3.6, 3.7, 3.8, 3.9, 4.0)


def stats(*data):
    print("Level :", data[0])
    print("Health :", data[1])
    print("Mana :", data[2])
stats(10, 100, 50)


def rommate_info(*info):
    print("Name :", info[0])
    print("Age :", info[1])
    print("City :", info[2])
rommate_info("Yernar", 20, "Almaty")


def find_max(*numbers):
    return max(numbers)
print(find_max(5, 10, 15, 20, 25))


def requirement_steps(*steps):
    print("To get 100 % in this practical lesson complete the following steps:")
    print("Step 1:", steps[0])
    print("Step 2:", steps[1])
    print("Step 3:", steps[2])
requirement_steps("Complete tasks from W3School", "Write at least 5 examples of each topic", "Defend your code to the teacher")

# Examples of using **kwargs in Python functions.

def student_information(**info):
    print("Name:", info["name"])
    print("Course:", info["course"])
    print("Major:", info["major"])
student_information(name="Yernar", course= "1", major = "SITE")


def Work(Position, **details):
  print("Position:", Position)
  print("Required:")
  for key, value in details.items():
    print("  ", key + ":", value)
Work(
    "Reseptionist on 5 star hotel", 
     experience = "2 years", 
     skills = "Customer service, Communication, Multitasking", 
     Languages = "English, Russian, Kazakh"
     )


def car_information(brand, model, **specs):
    print("Car:", brand, model)
    print("Specifications:")
    for key, value in specs.items():
        print(" ", key + ":", value)
car_information(
    "Toyota",
    "Camry 3.5",
    engine="2.5L",
    color="White",
    year=2023,
    status="Не битый, не крашенный"
    )


def writing_resume(name, degree, **every_skill):
    print("Name : ", name) 
    print("Degree : ", degree)
    print("Skills : ")
    for key, value in every_skill.items():
        print(" ", value)
writing_resume(
    "Yernar", 
    "Bachelor's degree in Computer Science", 
    skill1 = "Python programming", 
    skill2 = "Data analysis", 
    skill3 = "Machine learning", 
    skill4 = "Problem-solving"
    )

# Example of using both *args and **kwargs in a Python function.

def event_information(event_name, *participants, **details):
    print("Event:", event_name)
    print("Participants:")
    for person in participants:
        print(" ", person)
    print("Details:")
    for key, value in details.items():
        print(" ", key + ":", value)
event_information(
    "Hackathon",
    "Yernar", "Aruzhan", "Dias",
    location="Astana",
    duration="24 hours"
    )


def register_user(username, **details):
    print("Username:", username)
    if "email" not in details:
        print("Error: Email is required")
        return
    print("User Details:")
    for key, value in details.items():
        print(" ", key + ":", value)
register_user("Yernar", email="ernarlo0p@gmail.com", age=19, country="Kazakhstan")

