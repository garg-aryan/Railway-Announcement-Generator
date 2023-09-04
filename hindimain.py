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
        
if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton1()
    print("Now Generating Announcement in Hindi: ")
    print()
    generateAnnouncement1("announce_hindi.xlsx")