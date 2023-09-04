# Code to generate announcement in English Only

import os
import pandas as pan
from pydub import AudioSegment
from gtts import gTTS

from main import mergeaudios2, textToSpeechEn

# it generates all the audio segment in english


def generateSkeleton2():
    audio2 = AudioSegment.from_mp3('railway.mp3')

    # 12 generate May I have your attention please
    start = 20000
    finish = 23500
    audioProcessed = audio2[start:finish]
    audioProcessed.export("12_English.mp3", format="mp3")

    #  13 train number and name

    # 14 From
    start = 30000
    finish = 31000
    audioProcessed = audio2[start:finish]
    audioProcessed.export("14_English.mp3", format="mp3")

    # 15 is city

    # 16 Generate to
    start = 31500
    finish = 32500
    audioProcessed = audio2[start:finish]
    audioProcessed.export("16_English.mp3", format="mp3")

    # 17 is destination city

    # 18 Generate via
    start = 33500
    finish = 34500
    audioProcessed = audio2[start:finish]
    audioProcessed.export("18_English.mp3", format="mp3")

    # 19 is via city name

    #  20 - generate is arriving om platform no
    start = 36500
    finish = 40200
    audioProcessed = audio2[start:finish]
    audioProcessed.export("20_English.mp3", format="mp3")

    #  21 is platform number

    # 22 - generate tututu
    start = 40800
    finish = 42300
    audioProcessed = audio2[start:finish]
    audioProcessed.export("22_English.mp3", format="mp3")

def generateAnnouncement2(filename):
    df1 = pan.read_excel(filename)
    print(df1)
    for index, item in df1.iterrows():
        # 2 generate from city
        textToSpeechEn(item['train_no']+" " +
                       item['train_name'], '13_English.mp3')

        # 4 generate via city
        textToSpeechEn(item['via'], '19_English.mp3')

        # 6 generate to city
        textToSpeechEn(item['to'], '17_English.mp3')

        # 8 generate train no and name
        textToSpeechEn(item['from'], '15_English.mp3')

        # 10 generate platform no
        textToSpeechEn(item['platform'], '21_English.mp3')

        audios2 = [f"{i}_English.mp3" for i in range(12, 23)]
        announcement = mergeaudios2(audios2)
        announcement.export(
            f"English_announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton2()
    print("Now Generating Announcement in English: ")
    print()
    generateAnnouncement2("announce_hindi.xlsx")