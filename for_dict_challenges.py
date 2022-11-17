# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???        
count_names = {}        
        
for student in students:
    name = student.get('first_name')
    if name in count_names:
        count_names[name] += 1
    else:
        count_names[name] = 1

for key in count_names:
    print(f"{key}: {count_names[key]}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
count_names = {}        
        
for student in students:
    name = student.get('first_name')
    if name in count_names:
        count_names[name] += 1
    else:
        count_names[name] = 1
        
common_name = max(count_names, key=count_names.get)

print(common_name)

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
for class_number, students in enumerate(school_students, start=1):
    count_names = {} 
    
    for student in students:
        name = student.get('first_name')
        if name in count_names:
            count_names[name] += 1
        else:
            count_names[name] = 1
            
    common_name = max(count_names, key=count_names.get)
            
    print(f'Самое частое имя в классе {class_number}: {common_name}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
for school_class in school:
    students = school_class.get('students')
    girls = 0
    boys = 0
    
    for name in students:
        if is_male.get(name['first_name']):
            boys += 1
        else:
            girls += 1
            
    print(f"Класс {school_class['class']}: девочки {girls}, мальчики {boys}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
count_boys_in_class = {}
count_girls_in_class = {}

for school_class in school:
    students = school_class.get('students')
    girls = 0
    boys = 0
    
    for name in students:
        if is_male.get(name['first_name']):
            boys += 1
        else:
            girls += 1
    
    count_boys_in_class[school_class['class']] = boys
    count_girls_in_class[school_class['class']] = girls
    
common_boys = max(count_boys_in_class, key=count_boys_in_class.get)
common_girls = max(count_girls_in_class, key=count_girls_in_class.get)

print(f'Больше всего мальчиков в классе {common_boys}')
print(f'Больше всего девочек в классе {common_girls}')
