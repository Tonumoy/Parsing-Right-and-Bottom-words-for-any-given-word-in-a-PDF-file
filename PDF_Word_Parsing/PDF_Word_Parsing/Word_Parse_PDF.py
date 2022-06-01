# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author - Tonumoy
"""

import pytesseract
from pdf2image import convert_from_path


# Setting the Path of pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\tesseract'

 
# Setting the I/P & O/P file paths
path="C:/Users/tonum/OneDrive/Desktop/Codes/PDF_Word_Parsing/" #input folder path
output_folder_path="C:/Users/tonum/OneDrive/Desktop/Codes/PDF_Word_Parsing/"
pdfname=path+"sample.pdf"

# Counting the number of pages in the pdf and converting the pages into image
images = convert_from_path(pdfname)
i = 1
l=len(images)
print("Number of pages in PDF="+str(l))
for image in images:
	image.save(output_folder_path + str(i) + '.jpg', 'JPEG')
	i = i + 1

# converting image into text
text = pytesseract.image_to_string(image) #converting into text

# initializing punctuations string
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for ele in text:
    if ele in punc:
        text = text.replace(ele, "")

# writng output as a text file
with open("Output.txt", "w") as text_file:
    text_file.write(text) 

text_words = text.split()
text_lines = text.split('\n')
text_lines_filtered = list(filter(None,text_lines))
text_lines_filtered_new = [j.split(' ') for j in text_lines_filtered]

value = "cried" #any word
 
#printing the right word
if value in text_words:
    pos = text_words.index(value) #first instance of any word    
print("The Word on the right of the given word is:",text_words[pos+1])



# finding sentence number and word position

for i,sen in enumerate(text_lines_filtered_new):
    if value in sen:
        wrd_pos = text_lines_filtered_new[i].index(value)
        break

strpos = text_lines_filtered[i].find(value) # character position of word

# finding all word positions in next line
pos = []
#for i, sen in enumerate(text_lines_filtered_new):
for word in text_lines_filtered_new[i+1] :
    p = text_lines_filtered[i+1].find(word)
    pos.append(p)

# word position in the next line
for j,p1 in enumerate(pos):
    if strpos <= p1:
        wrd_pos2 = max(0,j-1)
        break
print("The Word below the given word is:", text_lines_filtered_new[i+1][wrd_pos2])   
    

