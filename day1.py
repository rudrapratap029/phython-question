#cerate a dictionary of 5 contries and their capitals. print it
countries_and_capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "India": "New Delhi",
    "Spain": "Madrid",
    "Japan": "Tokyo"
}
print(countries_and_capitals)

#access the capital of India from the dictionary.
print("The capital of India is:", countries_and_capitals["India"])

#add a new key-value pair "Italy: Rome" to the dictionary.
countries_and_capitals["Italy"] = "Rome"
print("Updated dictionary:", countries_and_capitals)

#Update the capital of Germany to "Munich".
countries_and_capitals["Germany"] = "Munich"
print("Updated capital of Germany:", countries_and_capitals["Germany"])


#Delete the key of france using del
del countries_and_capitals["France"]
print("Dictionary after deleting France:", countries_and_capitals)


#Dictionary methods
#create a dictionary of students and their marks. Use .keys() to print all the student names.
students_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}
print("Student names:", students_marks.keys())


#Use .values() to print all the marks.
print("Student marks:", students_marks.values())

#Use .items() to print all the key-value pairs.
print("Student marks items:", students_marks.items())


#use .get() to access the value of "Rahul" Safely (if not found return "Not Found")
print("Marks of Rahul:", students_marks.get("Rahul", "Not Found"))

#Use .update() to add multiple key-value pairs in one step
students_marks.update({
    "Eve": 88,
    "Frank": 76
})
print("Updated student marks:", students_marks)

#Removing Elements
#Use  .pop(key) to remove "Germny" form the dictonary
removed_capital = countries_and_capitals.pop("Germany", "Not Found")
print("Removed capital of Germany:", removed_capital)


#Try poping an non existing using .pop() with default value
removed_capital_non_existing = countries_and_capitals.pop("Brazil", "Not Found")
print("Trying to remove non-existing country Brazil:", removed_capital_non_existing)


#Use .clear() to remove all items from the dictionary
students_marks.clear()
print("Students marks after clearing:", students_marks)
