import requests
import json
import random
import speech_recognition as sr

from PIL import Image
from io import BytesIO 


def random_name():
    id = random.randint(1,110)
    url = f'https://rickandmortyapi.com/api/character/{id}'
    response = requests.get(url)
    response = response.json()

    with open("id_random.json", "w") as file:
        json.dump(response, file)
    file.close()
    with open("id_random.json","r") as file:
        data = json.load(file)
    print("Name_character: " + data["name"])
    
# random_name()

def save_image():
    with open("id_random.json", "r") as file:
        data = json.load(file)
        # print(data["image"])
        url = data["image"]
        response = requests.get(url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image.save('image.jpeg')
            
# save_image()

def show_name_episode():
    with open("id_random.json", "r") as file:
        data = json.load(file)
        url = data["episode"]
        url = url[0]
        response = requests.get(url)
        
        data = response.json()
        print("Name episode: " + data["name"])
    
# show_name_episode()

def show_image():
    with open("id_random.json", "r") as file:
        data = json.load(file)
        # print(data["image"])
        url = data["image"]
        response = requests.get(url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image.show()
            
# show_image()

def resolution():
    image = Image.open("image.jpeg")
    width, height = image.size
    print("Image resolution: " + str(width) + "x" + str(height) + " pixel ")
        
# resolution()


def main():
    # Инициализировать распознаватель (распознавание речи)
    r = sr.Recognizer()

    # Используйте микрофон, чтобы услышать голос
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    text = ""

    try:
        text += r.recognize_google(audio, language='en-US')
    except sr.UnknownValueError:
        print("Unable to recognize voice")
    except sr.RequestError as e:
        print("Error during offline speech recognition: {0}".format(e))
        
    # print(text)
    if text == "random":
        random_name()
    elif text == "save":
        save_image()
    elif text == "episode":
        show_name_episode()
    elif text == "show":
        show_image()
    elif text == "resolution":
        resolution()
    else:
        print("Invalid request !!!")

main()