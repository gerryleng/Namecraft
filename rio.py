from guizero import *
import sys
import random
from random import choice
import string
import pyperclip
import datetime

time = datetime.datetime.now()
alp = string.ascii_letters
num = string.digits
sym = "!@#$%^&*"
characters = list(alp + num + sym)

print("Welcome to Rio !", time)

def lucky_number():
    ln = "Lucky Number➼" + "❤" + choice(num) + choice(num) + "\nMaker➼❤lenX"

    ln_text = Text(rio, text=ln)
    ln_text.font = "Ink Draft"
    ln_text.text_color = "pink"
    ln_text.text_size = "10"



class UsernameGenerator:
    def __init__(self):
        min_length, max_length = 0, 0
        try:
            max_length = int(sys.argv[2])
        except IndexError:
            is_ranged = False
        else:
            is_ranged = True

        try:

            if is_ranged:
                min_length = int(sys.argv[1])
            else:
                length = int(sys.argv[1])
        except IndexError:
            length = 7
        self.consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                           'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
        self.vowels = ('a', 'e', 'i', 'o', 'u')
        self.cons_weighted = (("t", "n"), ("r", "s", "h", "d"), ("l", "f", "c", "m"), ("g", "y", "p", "w", "b"),
                              ("v", "b", "j", "x", "q"), "z")
        self.vow_weighted = (("e", "a", "o"), ("i", "u"))
        self.double_cons = ("he", "re", "ti", "ti", "hi", "to", "ll", "tt", "nn", "pp", "th", "nd", "st", "qu")
        self.double_vow = ("ee", "oo", "ei", "ou", "ai", "ea", "an", "er", "in",
                           "on", "at", "es", "en", "of", "ed", "or", "as")
        for i in range(10):
            username, is_double, num_length = "", False, 0
            is_consonant = random.randrange(10) > 0
            if is_ranged:
                length = random.randrange(min_length, max_length)
            if random.randrange(5) == 0:
                num_length = random.randrange(3) + 1
                if length - num_length < 2:
                    num_length = 0
            for j in range(length - num_length):
                if len(username) > 0:
                    if username[-1] in self.consonants:
                        is_consonant = False
                    elif username[-1] in self.consonants:
                        is_consonant = True
                if not is_double:
                    if random.randrange(8) == 0 and len(username) < int(length - num_length) - 1:
                        is_double = True
                    if is_consonant:
                        username += self.get_consonant(is_double)
                    else:
                        username += self.get_vowel(is_double)
                    is_consonant = not is_consonant
                else:
                    is_double = False
            if random.randrange(2) == 0:
                username = username[:1].upper() + username[1:]
            if num_length > 0:
                for j in range(num_length):
                    username += str(random.randrange(10))
            username_text = Text(window_username, text=username)
            username_text.text_color=color_text
            username_text.font = "Comic Sans MS Bold"
    def get_consonant(self, is_double):
        if is_double:
            return random.choice(self.double_cons)
        else:
            i = random.randrange(100)
            if i < 40:
                weight = 0
            elif 65 > i >= 40:
                weight = 1
            elif 80 > i >= 65:
                weight = 2
            elif 90 > i >= 80:
                weight = 3
            elif 97 > i >= 90:
                weight = 4
            else:
                return self.cons_weighted[5]
            return self.cons_weighted[weight][random.randrange(len(self.cons_weighted[weight]))]

    def get_vowel(self, is_double):
        if is_double:
            return random.choice(self.double_vow)
        else:
            i = random.randrange(100)
            if i < 70:
                weight = 0
            else:
                weight = 1
            return self.vow_weighted[weight][random.randrange(len(self.vow_weighted[weight]))]

def password():
    length = 9
    random.shuffle(characters)
    password_list = []
    for i in range(length):
        password_list.append(random.choice(characters))
    random.shuffle(password_list)
    password_output = "".join(password_list)
    password_shown = Text(window_password, text=password_output)
    password_shown.text_color = color_text
    password_shown.font = "Comic Sans MS Bold"
    pyperclip.copy(password_output)

def choose():
    todo_list = [user_todo1.value, user_todo2.value, user_todo3.value]
    choice_output = random.choice(todo_list)
    choice_shown = Text(window_choice, text=choice_output)
    choice_shown.text_color = color_text
    choice_shown.font="Comic Sans MS Bold"


def password_window():
    window_password.show()
def username_window():
    window_username.show()
def choice_window():
    window_choice.show()

def highlight1():
    user_todo1.bg = "pink"
def lowlight1():
    user_todo1.bg = "black"
def highlight2():
    user_todo2.bg = "pink"
def lowlight2():
    user_todo2.bg = "black"
def highlight3():
    user_todo3.bg = "pink"
def lowlight3():
    user_todo3.bg = "black"

#Rio theme color
color_text = "#00ffff"
color_bg = "#1a1a1a"
pink = "#fa6f96"
purple = "#9f2196"


rio = App(title="Rio Dice", bg=color_bg, width="175", height="305")

rio_image = PushButton(rio, image="rio2.png", command=lucky_number)


text_welcome = Text(rio, "Rio Dice")
text_welcome.text_color= color_text
text_welcome.font = "Comic Sans MS Bold"
text_welcome.text_size = "15"

window_username = Window(rio, title="Username", bg=color_bg, width="175", height="305")
window_username.hide()
genuse_button = PushButton(window_username, text="Shake", command=UsernameGenerator, image="bet1.png", align="bottom")
genuse_button.bg="grey"


window_password = Window(rio, title="Password", bg=color_bg, width="175", height="305")
window_password.hide()

window_choice = Window(rio, title="Choice", width="175", height="305")
window_choice.hide()
window_choice.bg=color_bg


username_button = PushButton(rio, text="Username", command=username_window, width="8")
username_button.text_color = "white"
username_button.bg = "grey"
username_button.font = "Comic Sans MS Bold"


password_button = PushButton(rio, text="Password", command=password_window, width="8")
password_button.text_color= "white"
password_button.bg= purple
password_button.font = "Comic Sans MS Bold"

choice_button = PushButton(rio, text="Choice", command=choice_window, width="8")
choice_button.bg= pink
choice_button.text_color="white"
choice_button.font = "Comic Sans MS Bold"

password_output = PushButton(window_password, command=password, image="bet1.png", align="bottom")
password_output.bg = "purple"

user_todo1 = TextBox(window_choice)
user_todo1.bg = "pink"
user_todo1.when_mouse_enters = highlight1
user_todo1.when_mouse_leaves = lowlight1
user_todo2 = TextBox(window_choice)
user_todo2.bg = "pink"
user_todo2.when_mouse_enters = highlight2
user_todo2.when_mouse_leaves = lowlight2
user_todo3 = TextBox(window_choice)
user_todo3.bg = "pink"
user_todo3.when_mouse_enters = highlight3
user_todo3.when_mouse_leaves = lowlight3
choose_button = PushButton(window_choice, command=choose, image="bet1.png", align="bottom")
choose_button.bg = "pink"

rio.display()
print("thanks for using !")
