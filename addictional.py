import json
import requests

import speech_recognition as sr 


word = input("Enter a word: ")
url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

def meanings_and_examples():
    arr = []
    response = requests.get(url)
    response = response.json()
    response = response[0]
    data = response["meanings"]

    for i in range(len(data)):
        arr.append(data[i]["definitions"])
        
    arr_len = []
    for i in range(len(arr)):
        arr_len.append(len(arr[i]))

    new_arr = []
    for i in range(len(arr)):   
        for j in range(max(arr_len)):    
            try:
                new_arr.append(arr[i][j])
            except IndexError:
                pass
    
    dictionary = {}
    
    for i in range(len(new_arr)):
        # print(f"Definition[{i+1}]: " + new_arr[i]["definition"])
        dictionary[f"Definition[{i+1}]: "] = new_arr[i]["definition"]
        
        try:
            # print(f"Example[{i+1}]: " + new_arr[i]["example"] + "\n")
            dictionary[f"Example[{i+1}]: "] = new_arr[i]["example"]

        except KeyError:
            # print(f"Example[{i+1}]: NO EXAMPLE !!! \n")
            dictionary[f"Example[{i+1}]: "] = "NO EXAMPLE !!! \n"
        
        # with open("meanings.json", "w") as file:
        #     json.dump(dictionary, file)

    return dictionary

def get_links():
    response = requests.get()
    response = response.json()
    response = response[0]

    return  response["sourceUrls"][0]
# print(get_links())

def save():
    
    dictionary = meanings_and_examples()
    
    word_dict = {"word: ": word}
    link_dict = {"link: ": get_links()}
    
    word_dict.update(dictionary)
    word_dict.update(link_dict)
    
    with open("results.json", "w") as file:
        json.dump(word_dict, file)
    file.close()
# save()

def main():
    r = sr.Recognizer()

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

        if text == "save":
            save()
        elif text == "meaning" or text == "example":
            dictionary = meanings_and_examples()
            for key, value in dictionary.items():
                print(key + ": " +  value)
        elif text == "link":
            print("Link: ", end="")
            print(get_links())
        else:
            print("Invalid request!!!")

main()


  
        

        
        
        
        
        
        
