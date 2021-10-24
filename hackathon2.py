"""
Created on Sun Jun 28 15:15:42 2020
@author: grace
"""
# This program generates a wordcloud emotions by calling the audiototex function in audiototext
import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#from hackathon import calculate_frequencies
import pandas as pd
from os import path
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
from audiototext import audiototext

import text2emotion as te
import numpy as np
import speech_recognition as sr

from glob import glob
from os.path import exists, join
import shutil
#from ffmpeg import FFmpeg

from os import path
from pydub import AudioSegment




def get_type_files(dirs, filetype=None, recursive=False):
    if not exists(dirs):
        return "Error: No such file or dir:{}".format(dirs)
    if filetype is None:
        return "file_type needed!"
    if recursive:
        file_list = glob(join('**/*'+filetype), recursive=True)
    else:
        file_list = glob(join('*'+filetype), recursive=False)
    return file_list


if __name__ == '__main__':
    folder = r'C:\Users\grace\HTML-CSS-JAVASCRIPT\wordcloud.py'
    file_type = '.wav'

    result = get_type_files(folder, file_type, recursive=True)
    print(len(result), end='\n')
    for element in result:
        print('{}'.format(element))

    # print(result)
    text1 = result[0]
    newtext = ''

    for i in range(len(text1)):
        if(text1[i] == '\\'):
            newtext = text1[i+1:]
            # print(newtext)


# EDIT THIS ONCE WE HAVE A WAV FILE
filename = newtext
""" newnewtext = ''
while(newtext[i])
for i, char in newtext.enumerate(): """


text = audiototext(filename)  # call the function
print(text)

#text = ' am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling? This breeze, which has travelled from the regions towards which I am advancing, gives me a foretaste of those icy climes. Inspirited by this wind of promise, my daydreams become more fervent and vivid. I try in vain to be persuaded that the pole is the seat of frost and desolation; it ever presents itself to my imagination as the region of beauty and delight. There, Margaret, the sun is for ever visible, its broad disk just skirting the horizon and diffusing a perpetual splendour. There—for with your leave, my sister, I will put some trust in preceding navigators—there snow and frost are banished; and, sailing over a calm sea, we may be wafted to a land surpassing in wonders and in beauty every region hitherto discovered on the habitable globe. Its productions and features may be without example, as the phenomena of the heavenly bodies undoubtedly are in those undiscovered solitudes. What may not be expected in a country of eternal light? I may there discover the wondrous power which attracts the needle and may regulate a thousand celestial observations that require only this voyage to render their seeming eccentricities consistent for ever. I shall satiate my ardent curiosity with the sight of a part of the world never before visited, and may tread a land never before imprinted by the foot of man. These are my enticements, and they are sufficient to conquer all fear of danger or death and to induce me to commence this laborious voyage with the joy a child feels when he embarks in a little boat, with his holiday mates, on an expedition of discovery up his native river. But supposing all these conjectures to be false, you cannot contest the inestimable benefit which I shall confer on all mankind, to the last generation, by discovering a passage near the pole to those countries, to reach which at present so many months are requisite; or by ascertaining the secret of the magnet, which, if at all possible, can only be effected by an undertaking such as mine.'
emotion_dictionary = te.get_emotion(text)
print(emotion_dictionary)
cloud = wordcloud.WordCloud(background_color="white")
cloud1 = cloud.generate_from_frequencies(emotion_dictionary)

cloud2 = cloud1.to_array()
myimage = cloud2
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.savefig("new_wordcloud.png", format="png")
plt.show()
