# colored(text, color=None, on_color=None, attrs=None)
from termcolor import colored
from pyfiglet import figlet_format  # for stylized text
from colorama import init  # to support termcolor in powershell
import requests
from random import choice

style_text1 = figlet_format("Dad Joke 3000")
init()
style_text2 = colored(text=f'{style_text1}', color="cyan")
print(style_text2)

topic = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={
        "Accept": "application/json"},
    params={
        "term": topic}).json()

num_jokes = response['total_jokes']
jokes = response['results']
if not num_jokes:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again")
else:
    if num_jokes > 1:
        print(f"I've got {num_jokes} jokes about {topic}. Here's one:")
        result = choice(jokes)['joke']
        print(result)
    else:
        print(f"I've got one joke about {topic}. Here it is:")
        result = jokes[0]['joke']
        print(result)
