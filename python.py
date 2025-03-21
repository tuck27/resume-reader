'''# importing all the required modules
import pypdf
import re

# creating a pdf reader object
reader = pypdf.PdfReader('Hockey.pdf')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
print(reader.pages[0].extract_text())

string = "ice"

for page in reader.pages:
    text = page.extract_text()
    res_search = re.search(string, text)
    print(res_search)
'''

import pypdf
import re

# open the pdf file
reader = pypdf.PdfReader("Hockey.pdf")

# get number of pages
num_pages = len(reader.pages)

# define key terms
string1 = "players" #college education
string2 = "ice" #skills
string3 = "game" #experiences
string4 = "stick" #certifications

# extract text and do the search
for page in reader.pages:
    text = page.extract_text() 
    # print(text)
    res_search = re.findall(string1, text)
    len(res_search)
    print(res_search)
    res_search = re.findall(string2, text)
    len(res_search)
    print(res_search)
    res_search = re.findall(string3, text)
    len(res_search)
    print(res_search)
    res_search = re.findall(string4, text)
    len(res_search)
    print(res_search)

players_count = len(res_search)
ice_count = len(res_search)
game_count = len(res_search)
stick_count = len(res_search)

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
pdf = "Hockey.pdf"

'''def get_points_for_pdf(pdf: "Hockey.pdf")-> tuple:
    total_points = 0
    for word in pdf:
        if word in "players":
            total_points += 1
        elif word in "ice":
            total_points += 1
        elif word in "game":
            total_points += 1
        elif word in "stick":
            total_points += 1
    return (total_points, total_points / len(word))

print("Word                 | TOT | AVE ")
print("---------------------+-----+-----")
for word in "Hockey.pdf":
    total_points, average_points = get_points_for_pdf(word)
    print(f"{word:20} | {total_points:3} | {average_points:.3}")'''