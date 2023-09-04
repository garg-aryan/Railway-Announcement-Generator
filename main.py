# this file contains both the code in english as well in hindi

import os
import pandas as pan
from pydub import AudioSegment
from gtts import gTTS

# function to get text in hindi from file


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myObj = gTTS(text=mytext, lang=language, slow=False)
    myObj.save(filename)

# function to get text in english from file


def textToSpeechEn(text, filename):
    mytext2 = str(text)
    language = 'en'
    myObj1 = gTTS(text=mytext2, lang=language, slow=False)
    myObj1.save(filename)


# this function returns pydubs audio segment
def mergeaudios1(audios1):
    combined = AudioSegment.empty()
    for audio1 in audios1:
        combined += AudioSegment.from_mp3(audio1)
    return combined


def mergeaudios2(audios2):
    combined = AudioSegment.empty()
    for audio2 in audios2:
        combined += AudioSegment.from_mp3(audio2)
    return combined

# it generates all the audio segments in hindi


def generateSkeleton1():
    audio1 = AudioSegment.from_mp3('railway.mp3')
    # 1 generate kripya dhayan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio1[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    #  2 is from city

    # 3 Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio1[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 Generate ke raste
    start = 94000
    finish = 95000
    audioProcessed = audio1[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 Generate ko jane wali gaadi sankhya
    start = 96000
    finish = 98900
    audioProcessed = audio1[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 is train no and name

    #  9 - generate kuch hi samaye me platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio1[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    #  10 is platform number

    # 11 - generate pr aa rahi h
    start = 109000
    finish = 112250
    audioProcessed = audio1[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

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


def generateAnnouncement1(filename):
    df = pan.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 generate from city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 generate via city
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6 generate to city
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8 generate train no and name
        textToSpeech(item['train_no'] + " " +
                     item['train_name'], '8_hindi.mp3')

        # 10 generate platform no
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios1 = [f"{i}_hindi.mp3" for i in range(1, 12)]
        announcement = mergeaudios1(audios1)
        announcement.export(
            f"Hindi_announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


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
    generateSkeleton1()
    generateSkeleton2()
    print("Now Generating Announcement in Hindi: ")
    print()
    generateAnnouncement1("announce_hindi.xlsx")
    print()
    print("Now Generating Announcement in English: ")
    print()
    generateAnnouncement2("announce_hindi.xlsx")
