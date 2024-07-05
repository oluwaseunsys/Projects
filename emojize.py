#import module
import emoji
#ask for user input

def main():
    prompt = input("Input: ")
#try except statement in case of errors
    try:
        prompt = emoji.emojize(prompt)
        print(prompt)
    except ValueError:
        pass
#if the input is an alias for example, this else statement converts the prompt to an emoji
    else:
        prompt = emoji.emojize(prompt, language = "alias")
        print(prompt)


main()