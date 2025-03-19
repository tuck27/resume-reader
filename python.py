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
    res_search = re.search(string1, text)
    print(res_search)
    res_search = re.search(string2, text)
    print(res_search)
    res_search = re.search(string3, text)
    print(res_search)
    res_search = re.search(string4, text)
    print(res_search)