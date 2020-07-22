import os
import random
import time
from english_words import english_words_lower_alpha_set
from gtts import gTTS
import string


global score


def a_question():
    answers = list(english_words_lower_alpha_set)
    answer_true = answers[random.randint(0, 255)]
    random_chars = string.ascii_uppercase

    global score

    file = random.choice(random_chars)
    file = file + "file.mp3"
    tts = gTTS(answer_true)
    tts.save(file)
    os.system(file)


    answer_user = input("the spelling of said word is, *lowercase*:")
    if answer_user != answer_true:
        time.sleep(1)
        print()
        print("try again Bucciarati")
        os.remove(file)
    else:
        print()
        print("noice jobbo bobbo")
        score = score + 1
        os.remove(file)


score = 0
a_question()
a_question()
a_question()
a_question()
print("Your final score is:", score, "/ 4")
if score < 4:
    print("man you can't spell, what a dumbass")
if score == 4:
    print("wow great job you really....")
    time.sleep(2)
    print("speled?")

