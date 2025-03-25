
import pypdf
import re

# open the pdf file


'''
frequencyPointList = []
points1 = 0
points2 = 0
for words in ("Hockey.pdf"): 
    points1 = 0                                                                                    
    for word1 in words:
        if word1 in {"players"}:
            points1 += 1
        elif word1 in {"ice"}:
            points1 += 2
        elif word1 in {"game"}:
            points1 += 3
        elif word1 in {"stick"}:
            print("points1: " + str(points1))
            print(type(points1))
            numberWord1 = len(word1)
            print("numberWord1: " + str(numberWord1))
            print(type(numberWord1))
            points2 = (int(points1) // int(numberWord1))
            print("points2: " + str(points2))
            print(type(points2))
            frequencyPointList.append(points2)
'''
pdf = "resume1.pdf"

def get_points_for_pdf(text)-> tuple:
    total_points = 0
    for word in text:
        if word == "Leadership":
            total_points += 1
        elif word == "university":
            total_points += 1
        elif word == "Python":
            total_points += 1
        elif word == "GPA":
            total_points += 1
    return (total_points, total_points / len(word))

print("Word                 | TOT | AVE ")
print("---------------------+-----+-----")
for word in get_points_for_pdf(text):
    total_points, average_points = get_points_for_pdf(text)
    print(f"{word:20} | {total_points:3} | {average_points:.3}")