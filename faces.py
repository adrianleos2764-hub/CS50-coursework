#program converts emoticons to emojis from user input with emoticons 
def convert(text):
    # converts emoticons to emojis 
    text = text.replace(":)", "😊")
    text = text.replace(":(", "😞")
    return text


def main():
    # takes user input and converts emoticons to emojis with the convert function
    user_text = input("enter desired emoticon text: ")
    print(convert(user_text))

main()