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

#MR COOPER LOOK HERE
def get_points_for_pdf(text)-> tuple:
    total_points = 0
    for word in text:
        if word == "Leadership":
            total_points += 1
        if word == "university":
            total_points += 1
        if word == "Python":
            total_points += 1
        if word == "GPA":
            total_points += 1
    return (total_points, total_points / len(word))

print("Word                 | TOT | AVE ")
print("---------------------+-----+-----")
for word in extract_text(reader.pages):
    total_points, average_points = get_points_for_pdf(text)
    print(f"{word:20} | {total_points:3} | {average_points:.3}")