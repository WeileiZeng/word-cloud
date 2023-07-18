import numpy as np
# makes the circle using numpy
w=1000
r=w/2-20
x, y = np.ogrid[:w, :w]
mask = (x - w/2) ** 2 + (y - w/2) ** 2 > r ** 2
mask = 255 * mask.astype(int)



import os
from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
#d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()

# Generate a word cloud image
#wordcloud = WordCloud().generate(text)

#f={"hello":0.3,"world":0.7}

import json
#file created by json.dump(f,data)
with open("text.json","r") as data:
    f=json.load(data)


wc = WordCloud(background_color="white",width=100, height=100,
               mask=mask, contour_width=0.1, contour_color="black")
    
wordcloud = wc.fit_words(f)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
#plt.figure
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

plt.savefig("tmp.svg")
#plt.show()

# lower max_font_size
#exit()
#wordcloud = WordCloud(max_font_size=40).generate(text)
#plt.figure(figsize=(20,20))
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
