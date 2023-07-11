import numpy as np
# makes the circle using numpy
w=1000
r=w/2 -10
x, y = np.ogrid[:w, :w]
mask = (x - w/2) ** 2 * 2 + (y - w/2) ** 2  > r ** 2
mask = 255 * mask.astype(int)


from wordcloud import WordCloud


# Generate a word cloud image
#wordcloud = WordCloud().generate(text)

#f={"hello":0.3,"world":0.7}
import json
#file created by json.dump(f,data)
with open("weilei.json","r") as data:
    f=json.load(data)

#wc = WordCloud(background_color="white",width=100, height=100, mask=mask)#, contour_width=0.1, contour_color="blue")

wc = WordCloud(background_color="rgba(255, 255, 255, 0)",mode="RGBA",width=100, height=100, mask=mask)
    
wordcloud = wc.fit_words(f)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
#plt.imshow(wordcloud, interpolation='bilinear')
plt.imshow(wordcloud)
plt.axis("off")

plt.savefig("weilei.svg",bbox_inches='tight', transparent=True)


#plt.show()

# lower max_font_size
#exit()
#wordcloud = WordCloud(max_font_size=40).generate(text)

