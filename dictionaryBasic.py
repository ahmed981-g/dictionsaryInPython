# Course Detail
print('\n'*3)
course = {
    "title": "Web Development",
    "duration": "1 Year",
    "fee": "70k",
    "eligibility": "Basic Knowledge of Computer"
}
# Print Key value Pairs
print(type(course))

# Accessing value or key title
print(course["title"])

# Length of Value in Given Dictionary
print(len(course))
# Assign a single value to a variable
x = course["title"]

print(x)

# Other way to access specific Key value
x = course.get("fee")
print(x)

# Gettig all Keys in a Dictionary
print(course.keys())

# Updating Key value
course["fee"] = "35k"

# Printing After Updation
print(course.keys())


# Adding another key to existing dictionary

course['type'] = "Diploma"

print(course.keys())
print(course["type"])

# Getting all Values from a dictionary

print(course.values())

# Getting each item as key-value pair
y = course.items()
print(y)

# Converting key-value list into list of value or keys or key-value
itemsList = list(y)
valuesList = list(course.values())
keysList = list(course.keys())
print('\n')
print(itemsList[0][0])
print('\n')
print(valuesList)
print('\n')
print(keysList)

# Use 'in' keyword together with control flow to check existince of a key
print('\n\n')
if 'title' in course:
    print("Yes 'title' exit in the given dictionary.")

# Updating dictionary 

newCourse = {
    "title": "Web Designing",
    'duration': '6 Months',
    'fee': '12k',
    'eligibility': 'Metriculation or Xth or equivalent'
}
# Before Updation
print(course)
# After Updation

course.update(newCourse)
print(course)

# Empty Updation
course.update({'title':''})

print(course)

# REMOVE

# Removing last key-value

course.popitem()
print(course)

# Removing with known key
print('\n')
course.pop('title')

print(course)

# Removing with known key using dictionary key method

del course['fee']
print()

print(course)

# Deleting whole dictionary
print('-'*12)
del course
# print(course) # Will Cause NameError


# Empty an existing dictionary
print('-'*12)

newCourse.clear()

print(newCourse)



print('\n'*3)