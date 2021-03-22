# import reduce
from functools import reduce

# global variable to keep track of week
counter = 1

# declare lists
csv_raw = [] # list to import raw data
gradeList = [] # list to put in number data

# open CSV file
infile = open("grades.csv", 'r')
for line in infile:
    csv_raw.append(line.rstrip())

# separate by comma
gradeList = csv_raw[1].split(',')

def make_float(input):
    return float(input)

gradeList = map(make_float, gradeList)
def calc_score(input):
    global counter
    if counter == 8 or counter == 15:
        input *=0.3
    else:
        input = input * (0.4/13)
    counter+=1
    return input

def sum(a, b):
    return a + b



caliberated_score = map(calc_score, gradeList)
caliberated_score_list = list(caliberated_score)
print(caliberated_score_list)

total_score = reduce(sum, caliberated_score_list)
print(total_score)

def grade_assign(grade):
    if 90 <= grade <= 101: # 101 to cover for floating point precision limit
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 70 <= grade < 80:
        return 'C'
    elif 60 <= grade < 70:
        return 'D'
    elif grade < 60:
        return 'F'

print(grade_assign(total_score))
