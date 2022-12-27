# store 'Nina' as a string-type data in variable called "name"
name = 'Nina'
print(type(name))
print(f"The student's name is {name}.\n")

# store 45 as an integer-type data in variable called "pass_mark"
pass_mark = 45
print(type(pass_mark))
print(f"Minimum marks to pass is {pass_mark}\n")

# store 70.50 as a float-type data in a variable called "marks"
result_marks = 70.50
print(type(result_marks))
print(f"They scored {result_marks} in Maths\n")

# the comparator gives a boolean result
# stored in variable called "passed"
passed = (result_marks >= pass_mark)
print(type(passed))
print(f"{name} Passed the exam.: {passed}")

