import google.generativeai as palm
import os

def DogChat():
    chat_count = 10
    while chat_count >= 0:
        palm.configure(api_key=os.environ["PALM_KEY"])
        if chat_count == 10:
            user_input = input("Your message: ")
            response = palm.chat(context='Be a happy dog who is just overjoyed to be talking', messages=user_input)
        else:  
            response = response.reply(input("Your message: "))

        print(response.last)
        chat_count -= 1

    # print(response)
    
print(DogChat())