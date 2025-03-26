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
<<<<<<< HEAD
=======
reader = pypdf.PdfReader("resume1.pdf")

# get number of pages
num_pages = len(reader.pages)

# define key terms
string1 = "leadership" #college education
string2 = "university" #skills
string3 = "python" #experiences
string4 = "GPA" #certifications

# extract text and do the search
for page in reader.pages:
    text = page.extract_text() 
    # print(text)
    res_search = re.findall(string1, text)
    print(res_search)
    res_search = re.findall(string2, text)
    print(res_search)
    res_search = re.findall(string3, text)
    print(res_search)
    res_search = re.findall(string4, text)
    print(res_search)
>>>>>>> 7c49250 (finish commit)

my_dict = {"leadership": 1, "university": 2, "python": 3, "GPA": 4}

<<<<<<< HEAD
print("Word                 | TOT | AVE ")
print("---------------------+-----+-----")
for word in extract_text(reader.pages):
    total_points, average_points = get_points_for_pdf(text)
    print(f"{word:20} | {total_points:3} | {average_points:.3}")
=======
def get_points_for_pdf(words):
    total_points = 0
    for word in words:
        if word in my_dict:
            total_points += my_dict[word]
    return total_points

# extract text and calculate the score
for page in reader.pages:
    text = page.extract_text()
    words = text.split()  # Split the text into individual words
    total_points = get_points_for_pdf(words)
    print(f"Total points for this page: {total_points}")
>>>>>>> 7c49250 (finish commit)
