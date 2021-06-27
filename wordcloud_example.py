#!/usr/bin/env python3

import wordcloud
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import os
import sys

os.chdir(sys.path[0])

#Write the name of your text file, from which you wish to make a WordCloud, instead of filename below. For example, 'test.txt'

text = open(sys.argv[1], 'r', encoding='utf-8').read()

def calculate_frequencies(text):

#I needed my own list of uninteresting words to remove from my WordCloud and customize it for different texts that I used. You are more than welcome to remove or append the words that you don't want the WC to show.

    uninteresting_words = ["the", "however", "hundred", "kept", "saying", "may", "come", "either", "rather",
    "up", "every", "though", "thus", "since", "before", "most", "than", "about", "put", "these", "then", "say",
    "because", "therefore", "off", "could", "into", "having", "on", "take", "after", "said", "on", "himself", "men",
    "should", "upon", "other", "out", "only", "now", "many", "so", "yet", "not", "one", "for", "would", "made", "those",
    "there", "a", "in", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "none", "once", "large", "set", "indeed", "shall", "number",
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    sentence = ""
    interesting_words = []
    dict_count = {}
#Remove the punctuation from the text and generate a list of words:
    for x in text:
        if x.isalpha() or x == " ":
            sentence += x.lower()

#Remove the uninteresting words from the list of words so we are left with only
#interesting words.

    for word in sentence.split():
        if word not in uninteresting_words:
            interesting_words.append(word)

#We add the interesting words to the dictionary

    for word in interesting_words:
        if word not in dict_count:
            dict_count[word] = 0
        dict_count[word] += 1

#The custom mask is optional, you can comment out custom_mask if you don't want your WordCloud to have a particular appearance. I wanted mine to resemble the parthenon so I used a png image located in the same directory.
#All that you require is to write the name of the image file instead of imagefile. For example, 'testimage.png'

    custom_mask = np.array(Image.open(sys.argv[2]))

#Generate a wordcloud from our dictionary. You may determine the background color and if you chose not to have a mask you can remove it below. There are other parameters you can adjust and I recommend you check the documentation.

    cloud = wordcloud.WordCloud(background_color = 'white', mask = custom_mask)
    cloud.generate_from_frequencies(dict_count)

#The interpolation will adjust the smoothness of our image. You may choose your own and see what it might look like in the documentation(https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html)
#Let's remove the x and y axis that would otherwise appear on our image.
#We can see the WC image with plt.show().

    plt.imshow(cloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.show()

calculate_frequencies(text)
