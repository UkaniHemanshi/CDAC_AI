set_1_math = {'Alice','Bob','Charlie','David'}
set_2_science = {'Charlie','David','Eve','Frank'}

print(f"The student list who are enrolled in either 'Math' or 'Science' are: {set_1_math.union(set_2_science)} ")
print(f"The students list who are enrolled in both 'Math' and 'Science' are: {set_1_math.intersection(set_2_science)}")
print(f"The students list who are enrolled in 'Math' but not in 'Science' are: {set_1_math.difference(set_2_science)}")
print(f"The students list who are enrolled in 'Science' but not in 'Math' are: {set_2_science.difference(set_1_math)}")

print(set_2_science.symmetric_difference(set_1_math))