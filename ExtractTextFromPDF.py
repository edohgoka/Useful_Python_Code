# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:01:31 2020

@author: goka
"""

""" 

This is the best module to extract the text from a PDF file

"""

import fitz 

with fitz.open(r'Your_PDF_File_Name.pdf') as doc:
    text = ""
    for page in doc:
        text += page.getText()

print(text)

with open(r'myText2.txt', "w") as f:
        f.writelines(str(text.encode("utf-8")))

content2 = open(r'D:\DataScience\myText2.txt', "r").read()

content2 = content2.replace('\\n', '')

content2 = content2.replace('\\xe2', '')


unWantedWords = ['\\n', '\\xe2', '\\x80', '\\x9d', 'e. g.', 'pp', '\\xbf', '\\xef', '\\x88', '\\xa9', '\\x9986',
                 '\\x93760', 'D', 'J', '\\x93', '\\x8e', '\\x9cA', '\\x939', 'IEEE', '\\x9c', '\\xc3',
                 '\\xc3nay', 'en\\xc5ux', 'en\\xc5ux', '\\x81ngelesGil', 'Int', 'Conf', 'Y',
                 '\\xc2', '\\xb7', 'xcbY', 'et', 'al', 'N', 'X', 'W']
content3 = content2

for unword in unWantedWords:
    content3 = content3.replace(unword, '')
    
###############################################################################
########### •WORD CLOUD  ######################################################
###############################################################################
    
###☺ Creating the word cloud from the PDF 

# Import all the essentials libraries for word cloud 

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt 

# load list of common words to remove 
stopwords = set(STOPWORDS)

# open the file and read it into a variable named as content
content = open(r'D:\DataScience\myText.txt', "r").read()

# Instantiate a word cloud object 
content_wc = WordCloud(background_color="white", max_words=1000, contour_width=3,
                      contour_color='steelblue', width=600, height=400,
                      stopwords = stopwords
                      )

# Generate the word cloud 
content_wc.generate(content3)

## Generate the image 
#content_wc.to_image()

# Display the word cloud 
plt.imshow(content_wc, interpolation='bilinear')
plt.axis("off")
plt.show()
    
    
