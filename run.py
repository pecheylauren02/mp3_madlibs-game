'''
Imports modules and libraries for the game
'''
import sys
import time
import textwrap
import os
from os import system, name
import colorama
from colorama import init, Fore, Back, Style


def typewriter_print(text, color=None):
    '''
    Creates color and style condition
    Creates typewriter timer effect for text
    '''
    if color:
        text = getattr(Fore, color.upper()) + text + Style.RESET_ALL
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)


def clear_terminal():
    '''
    Clears terminal for better user experience
    '''
    system('cls' if name == 'nt' else 'clear')


class color:
    '''
    Declares all color and style variables
    '''
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


def start_game():
    '''
    Displays welcome message and instructions
    Starts the game after user enters "Y"
    '''
    typewriter_print(color.BOLD + color.GREEN + textwrap.dedent("""\
                     WELCOME to the maddest game
                     of Mad Libs you will ever play!\n
                     """ + color.END))
    typewriter_print(color.BOLD + color.YELLOW +
                     "What are Mad Libs?\n" + color.END)
    typewriter_print(color.BOLD + textwrap.dedent("""\
                     Mad Libs are stories with words
                     removed and replaced by blank spaces.\n
                     """))
    typewriter_print(textwrap.dedent("""\
                     It is also one of the world's greatest
                     word games and can turn anyone into the
                     funniest person in the room!\n
                     """))
    typewriter_print(textwrap.dedent("""\
                     So if you are looking for a night
                     of laughter and fun with your friends
                     and family, then look no further!\n
                     """) + color.END)

    # Instructions Section
    response = input(color.BOLD + color.GREEN +
                     "Want to learn how to play? Y/N: \n"
                     + color.END)

    while response.upper() not in ("Y", "N"):
        typewriter_print(color.BOLD + color.RED +
                         "\nInvalid response. Please enter Y or N.\n"
                         + color.END)
        response = input(color.BOLD + color.GREEN +
                         "Want to learn how to play? Y/N: \n"
                         + color.END)
    if response.upper() == "Y":
        clear_terminal()
        print(color.BOLD + color.YELLOW +
              "\nHere's how to play:\n" + color.END)
        typewriter_print(color.BOLD + textwrap.dedent("""\
                         1. Choose a story title from the list given,
                            by entering the number of the title.\n
                            """))
        typewriter_print(textwrap.dedent("""\
                         2. You must answer 20 prompts which will
                            ask you to enter words (E.g. "Enter a noun")
                            for your story, but you will not be allowed
                            to read the story beforehand.\n
                            """))
        typewriter_print(textwrap.dedent("""\
                         3. The prompts will ask you for a mix of adjectives,
                            nouns, exclamations, colours, adverbs, and more!\n
                            """))
        typewriter_print(textwrap.dedent("""\
                         4. When you finish entering all of the prompts
                            correctly, your story will then be
                            displayed for you to read aloud with
                            hilarious results.\n
                            """))
        typewriter_print(color.BOLD + color.CYAN + textwrap.dedent("""\
                         5. Remember: There are no winners or losers
                            in this game, only laughter!
                            """) + color.END)

        play_response = input(color.BOLD + color.GREEN +
                              "\nReady to play? Y/N: \n" + color.END)
        while play_response.upper() not in ("Y", "N"):
            print(color.BOLD + color.RED +
                  "Invalid response. Please enter Y or N.\n" + color.END)
            play_response = input(color.BOLD + color.GREEN +
                                  "\nReady to play? Y/N: \n" + color.END)
        if play_response.upper() == "N":
            clear_terminal()
            print(color.BOLD + textwrap.dedent("""\
                  Okay, maybe next time!\n
                  If you change your mind, just
                  press the "Run Terminal"
                  button to get started!\n
                  """ + color.END))
            sys.exit(0)
        else:
            clear_terminal()
            print(color.BOLD + color.CYAN + textwrap.dedent("""\
                  Let the Madness begin!
                  """) + color.END)
            play_madlibs()

    # allows user to skip instructions
    elif response.upper() == "N":
        clear_terminal()
        print(color.BOLD + color.CYAN +
              "\nWe love to see an experienced Mad Libber!\n"
              + color.END)
        play_madlibs()
    else:
        print(color.BOLD + textwrap.dedent("""\
              Okay, maybe next time!\n
              If you change your mind, just
              press the "Run Terminal"
              button to get started!\n
              """ + color.END))
        sys.exit(0)


def play_madlibs():
    '''
    Prints story titles for user to choose from
    Asks the user to select a story title
    Launches the game once the user enters inputs
    '''
    story_titles = ["A Peculiar Adventure",
                    "A Strange Fairytale",
                    "A Day at the Office",
                    "One Interesting Vacation",
                    "A Scary Encounter",
                    "A Day at the Beach",
                    "My First Day at School",
                    "A Wild Party"]

    typewriter_print(color.BOLD + color.YELLOW + textwrap.dedent("""\
                     Below is a list of story titles
                     for you to choose from:\n
                     """) + color.END)
    for i, title in enumerate(story_titles):
        print(color. BOLD + f"{i+1}. {title}\n")

    selected_story_index = None
    while selected_story_index is None:
        user_input = input(color.BOLD + color.GREEN + textwrap.dedent("""\
                           Enter the number of the story
                           you'd like to read: \n
                           """) + color.END)
        if user_input.isnumeric() and 1 <= int(user_input) <= 8:
            selected_story_index = int(user_input) - 1
            clear_terminal()
        else:
            print(color.BOLD + color.RED +
                  "Invalid input. Please enter a number between 1 and 8.\n"
                  + color.END)

    selected_story_title = story_titles[selected_story_index]

    print(color.BOLD + color.YELLOW + textwrap.dedent(f"""\
          You have selected the story: {selected_story_title}
          """ + color.END))
    # Story One
    if selected_story_title == "A Peculiar Adventure":

        words = ['an adjective, e.g. "pretty"', 'a feeling',
                 'a noun, e.g. "dog" or "table"', 'a place, e.g. "park"',
                 'another adjective', 'an animal',
                 'a noun, e.g. "dog" or "table"',
                 'another adjective', 'a verb ending in -ed, e.g. "jumped"',
                 'a plural noun, e.g. "dogs"', 'another adjective',
                 'an adverb, e.g. quickly',
                 'a feeling', 'another noun', 'another noun',
                 'another feeling', 'a number, e.g. "fifty seven"',
                 'another adjective',
                 'another feeling', 'a verb, e.g. "run"']

        inputs = []
        counter = 0
        for word in words:
            while True:
                user_input = input(color.BOLD +
                                   f"\nEnter {word}: \n" + color.END)
                if user_input.isdigit() or user_input.strip() == "":
                    print(color.BOLD + color.RED +
                          f"Invalid input. Please enter {word}.\n"
                          + color.END)
                elif len(user_input) <= 2:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too short.
                          Please try again.
                          """) + color.END)
                elif len(user_input) >= 20:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too long.
                          Please try again.
                          """) + color.END)
                else:
                    inputs.append(user_input)
                    counter += 1
                    if counter == 5:
                        clear_terminal()
                        counter = 0
                    break
        clear_terminal()
        print(color.BOLD + color.YELLOW +
              "Here is your creation!" + color.END)

        story_one = f"""
        One {inputs[0]} day, I woke up feeling {inputs[1]}
        and decided to go on a crazy adventure. I grabbed my trusty
        {inputs[2]} and set off into the {inputs[3]} wilderness. As I walked,
        I came across a {inputs[4]} {inputs[5]} who asked me for help.
        'I've lost my {inputs[6]}!' they exclaimed.\n
        Being the {inputs[7]} person I am, I offered to help.
        We {inputs[8]} high and low, through dense forests and mysterious
        {inputs[9]}, until finally we found the missing {inputs[6]}.
        The {inputs[6]} was so {inputs[10]} that we couldn't
        resist taking a selfie {inputs[11]} with it. Feeling
        {inputs[12]}, I said goodbye to my new friend, {inputs[5]},
        and continued on my wild adventure.\n
        Soon, I stumbled upon a giant {inputs[13]} who challenged me to
        a {inputs[14]} contest. I was feeling {inputs[15]}, so I accepted. We
        went back and forth, with each of us throwing {inputs[16]}
        punches at each other. In the end, I emerged victorious,
        much to the {inputs[17]} disappointment of my opponent.
        Exhausted but {inputs[18]}, I returned home and went straight
        to bed.\n
        As I drifted off to {inputs[19]}, I couldn't help but think
        that it had been a truly remarkable day. So if you're
        feeling {inputs[1]} and in need of an adventure,
        grab your {inputs[2]} and set off into the
        {inputs[10]} unknown. Who knows
        what kind of {inputs[7]} and {inputs[4]} things you might find
        along the way!\n\n"""

        typewriter_print(color.BOLD + textwrap.dedent(story_one))
        restart_game()

    # Story Two

    elif selected_story_title == "A Strange Fairytale":

        words = ['an adjective, e.g. "pretty"', 'a noun, e.g. "dog" or "mat"',
                 'a verb ending in -ing, e.g. "running"',
                 'another verb', 'a place, e.g. "park"', 'another adjective',
                 'another noun', 'another verb', 'another adjective',
                 'another noun', 'an exclamation, e.g. "Wow!"',
                 'another adjective', 'a verb ending in -ed, e.g. jumped',
                 'another verb ending in -ing', 'an adverb, e.g. quickly',
                 'another noun', 'another verb ending in -ed',
                 'a holiday, e.g. "Christmas"', 'a number, e.g. "fifty seven"',
                 'another adjective']

        inputs = []
        counter = 0
        for word in words:
            while True:
                user_input = input(color.BOLD +
                                   f"\nEnter {word}: \n" + color.END)
                if user_input.isdigit() or user_input.strip() == "":
                    print(color.BOLD + color.RED +
                          f"Invalid input. Please enter {word}.\n"
                          + color.END)
                elif len(user_input) <= 2:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too short.
                          Please try again.
                          """) + color.END)
                elif len(user_input) >= 20:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too long.
                          Please try again.
                          """) + color.END)
                else:
                    inputs.append(user_input)
                    counter += 1
                    if counter == 5:
                        clear_terminal()
                        counter = 0
                    break
        clear_terminal()
        print(color.BOLD + color.YELLOW +
              "Here is your creation!" + color.END)

        story_two = f"""
        Once upon a time, in a land far,
        far away, there was a {inputs[0]} {inputs[1]} who
        loved to {inputs[2]}. One day, while {inputs[3]} in
        the {inputs[4]}, the {inputs[0]} {inputs[1]}
        stumbled upon a {inputs[5]} {inputs[6]} who was {inputs[7]}
        with a {inputs[8]} {inputs[9]}.\n
        "Hey there, {inputs[10]}!" exclaimed the {inputs[0]}
        {inputs[1]}. "Would you like to join us in our
        {inputs[11]} {inputs[2]}?"\n
        Without hesitation, the {inputs[5]} {inputs[6]} agreed
        and soon found themselves {inputs[2]} with the
        {inputs[5]} {inputs[6]} and their {inputs[8]} {inputs[9]}.
        They {inputs[12]} and {inputs[12]},
        and even did a little {inputs[13]} together.\n
        But then, out of nowhere, a {inputs[11]} {inputs[15]}
        appeared and started throwing things {inputs[14]} at them!
        The {inputs[0]} {inputs[1]} and the {inputs[5]} {inputs[6]}
        were afraid, but to their surprise, the {inputs[8]}
        {inputs[9]} stood tall and {inputs[16]} the {inputs[11]}
        {inputs[15]}.\n
        From {inputs[17]}, the {inputs[0]} {inputs[1]} made a
        promise to themselves to always be open to new and
        {inputs[19]} experiences and never to be afraid of
        a little {inputs[2]}. And who knows? Maybe they'll
        even meet another {inputs[18]} {inputs[11]}
        {inputs[15]} along the way.
        The end\n\n"""

        typewriter_print(color.BOLD + textwrap.dedent(story_two))
        restart_game()

    # Story Three

    elif selected_story_title == "A Day at the Office":

        words = ['a feeling', 'a city', 'a noun, e.g. "dog" or "table"',
                 'another noun', 'an adjective, e.g. "pretty"',
                 'another feeling', 'a verb ending in -ing, e.g. "running"',
                 'another noun', 'another verb',
                 'a number, e.g. "fifty seven"', 'another adjective'
                 'another city', 'an adverb, e.g. quickly',
                 'another adjective', 'another noun', 'another adjective',
                 'a plural noun, e.g. "dogs"', 'another feeling',
                 'another noun', 'an item of clothing (plural)',
                 'another adjective']

        inputs = []
        counter = 0
        for word in words:
            while True:
                user_input = input(color.BOLD +
                                   f"\nEnter {word}: \n" + color.END)
                if user_input.isdigit() or user_input.strip() == "":
                    print(color.BOLD + color.RED +
                          f"Invalid input. Please enter {word}.\n"
                          + color.END)
                elif len(user_input) <= 2:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too short.
                          Please try again.
                          """) + color.END)
                elif len(user_input) >= 20:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too long.
                          Please try again.
                          """) + color.END)
                else:
                    inputs.append(user_input)
                    counter += 1
                    if counter == 5:
                        clear_terminal()
                        counter = 0
                    break
        clear_terminal()
        print(color.BOLD + color.YELLOW +
              "Here is your creation!" + color.END)

        story_three = f"""
        It was just another {inputs[0]} day in the office
        in {inputs[1]} when I arrived at my
        large {inputs[2]}. I sat down at my {inputs[2]}
        and opened up my {inputs[3]} to start my {inputs[4]} work.
        But before I could even begin, my {inputs[5]} coworker
        walked in and started {inputs[6]} loudly about their
        {inputs[7]} problems. I tried to tune them out, but their
        voice was so annoying that I couldn't {inputs[8]}.\n
        After what felt like {inputs[9]} hours of their constant
        {inputs[6]}, I decided to take a {inputs[10]}
        break and visit the office in {inputs[11]}.As I walked
        {inputs[12]} down the hallway, I noticed a {inputs[13]}
        smell coming from the break room. I cautiously peeked
        inside, and to my horror, I saw that someone had left
        their {inputs[14]} in the microwave for way too long.\n
        The {inputs[14]} was now a {inputs[15]} mess, and the
        entire room smelled like burnt {inputs[16]}.
        Feeling {inputs[17]}, I quickly made my way back to
        my {inputs[2]}, only to find that my {inputs[3]} had
        mysteriously disappeared! After a few minutes of
        searching {inputs[12]}, I finally found it hiding under
        a pile of dirty {inputs[18]}.\n
        So if you're ever feeling bored at work, just remember
        to keep your eyes and ears open for any weird moments
        that might come your way. You never know what kind of
        {inputs[15]} might be waiting just around the corner in
        {inputs[19]} {inputs[1]}!\n\n"""

        typewriter_print(color.BOLD + textwrap.dedent(story_three))
        restart_game()

    # Story Four

    elif selected_story_title == "One Interesting Vacation":

        words = ['a season', 'an adjective, e.g. "pretty"', 'a country',
                 'another adjective', 'a feeling', 'an item of clothing',
                 'another adjective', 'an adverb, e.g. quickly',
                 'a noun, e.g. "dog" or "table"', 'a plural noun, e.g. "dogs"',
                 'another adjective', 'an adverb, e.g. quickly',
                 'another noun', 'another feeling', 'a place, e.g. "park"',
                 'an exclamation, e.g. "Wow!"', 'another adjective',
                 'a verb ending in -ing, e.g. "running"',
                 'another verb ending in -ing', 'another noun']

        inputs = []
        counter = 0
        for word in words:
            while True:
                user_input = input(color.BOLD +
                                   f"\nEnter {word}: \n" + color.END)
                if user_input.isdigit() or user_input.strip() == "":
                    print(color.BOLD + color.RED +
                          f"Invalid input. Please enter {word}.\n"
                          + color.END)
                elif len(user_input) <= 2:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too short.
                          Please try again.
                          """) + color.END)
                elif len(user_input) >= 20:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too long.
                          Please try again.
                          """) + color.END)
                else:
                    inputs.append(user_input)
                    counter += 1
                    if counter == 5:
                        clear_terminal()
                        counter = 0
                    break
        clear_terminal()
        print(color.BOLD + color.YELLOW +
              "Here is your creation!" + color.END)

        story_four = f"""
        Last {inputs[0]}, I decided to take a {inputs[1]}
        vacation to {inputs[2]}, and boy was it {inputs[3]}!
        On the first day of my trip, I woke up feeling
        {inputs[4]} and ready for adventure. I threw
        on my {inputs[5]} and headed out into the {inputs[6]}
        unknown.\n
        As I walked {inputs[7]} through the streets, I came
        across a handsome {inputs[8]} who was juggling {inputs[9]}.
        I couldn't help but stop and watch in amazement as
        they threw the {inputs[9]} higher and higher into
        the air.\n
        After the {inputs[8]} finished their act, I decided
        to continue my {inputs[6]} journey. But before I could
        make it very far, a {inputs[10]} bird flew {inputs[11]}
        right into my {inputs[12]}! I was so startled that I nearly
        fell over, but luckily the bird flew away unharmed.\n
        Feeling a bit shaken and {inputs[13]}, I decided to take
        a break at a nearby {inputs[14]}. I ordered a {inputs[10]}
        drink and sat down to people-watch. That's when I heard
        a loud {inputs[15]} coming from outside. I opened my
        window and saw that a {inputs[16]} parade was going by!
        I quickly got dressed and joined the parade,
        {inputs[17]} and {inputs[18]} along to the music.\n
        It was so much fun that I almost forgot about my
        {inputs[19]}! I can't wait to see where my next crazy
        adventure takes me!\n\n"""

        typewriter_print(color.BOLD + textwrap.dedent(story_four))
        restart_game()

    # Story Five

    elif selected_story_title == "A Scary Encounter":

        words = ['an adjective, e.g. "pretty"', 'a noun, e.g. "dog" or "cup"',
                 'a verb ending in -ing, e.g. "running"',
                 'a feeling', 'another adjective', 'another adjective',
                 'an adverb, e.g. quickly', 'another adverb',
                 'an item of clothing',
                 'another noun', 'another adjective',
                 'another item of clothing',
                 'another verb ending in -ing',
                 'a body part', 'another feeling', 'another noun',
                 'another noun', 'another verb ending in -ing',
                 'another feeling', 'another feeling']

        inputs = []
        counter = 0
        for word in words:
            while True:
                user_input = input(color.BOLD +
                                   f"\nEnter {word}: \n" + color.END)
                if user_input.isdigit() or user_input.strip() == "":
                    print(color.BOLD + color.RED +
                          f"Invalid input. Please enter {word}.\n"
                          + color.END)
                elif len(user_input) <= 2:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too short.
                          Please try again.
                          """) + color.END)
                elif len(user_input) >= 20:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too long.
                          Please try again.
                          """) + color.END)
                else:
                    inputs.append(user_input)
                    counter += 1
                    if counter == 5:
                        clear_terminal()
                        counter = 0
                    break
        clear_terminal()
        print(color.BOLD + color.YELLOW +
              "Here is your creation!" + color.END)

        story_five = f"""
        One {inputs[0]} night, I was
        walking home from a {inputs[1]} party when I
        suddenly felt like someone was {inputs[2]} at me.
        I turned around, but there was no one there.
        Feeling a bit {inputs[3]}, I quickened my pace
        and started walking faster. But then, I heard a
        {inputs[4]} noise coming from behind me. I turned
        around again, and this time I saw a {inputs[5]}
        figure lurking {inputs[6]} in the shadows.\n
        I tried to run {inputs[7]}, but my {inputs[8]}
        got caught on a {inputs[1]}, and I fell to the
        ground. The {inputs[5]} figure approached me slowly,
        and I realized that it was actually a {inputs[9]}
        wearing a {inputs[10]} {inputs[11]}. I screamed for
        help, but no one seemed to hear me. The {inputs[9]}
        just stood there, {inputs[12]} at me with its tiny
        {inputs[13]}.\n
        Feeling {inputs[14]}, I tried to think of a way to
        escape. That's when I remembered the {inputs[15]}
        that I had in my {inputs[16]}. I pulled it out and
        aimed it at the {inputs[9]}, hoping that it would
        scare it away. To my surprise, the {inputs[9]} started
        {inputs[17]} and ran away as fast as it could. I got
        up and ran home as quickly as possible, feeling
        {inputs[18]} the entire time.\n
        As I lay in bed that night, I couldn't help but
        wonder what other {inputs[0]} encounters I might
        have in the future. But for now, I was just
        {inputs[19]} to be safe and sound in bed.\n\n"""

        typewriter_print(color.BOLD + textwrap.dedent(story_five))
        restart_game()

    # Story Six

    elif selected_story_title == "A Day at the Beach":

        words = ['an adjective, e.g. "pretty"', 'a type of holiday',
                 'another adjective', 'a plural noun, e.g. "dogs"',
                 'a vehicle, e.g. "car"', 'another plural noun',
                 'an adjective, e.g. "pretty"', 'a verb, e.g. "run"',
                 'another adjective', 'a verb ending in -ing, e.g. "running"',
                 'a body part', 'another noun', 'a place, e.g. "park"',
                 'another adjective', 'another noun',
                 'an adverb, e.g. quickly', 'another adjective',
                 'another noun', 'a type of animal',
                 'another verb ending in -ing']

        inputs = []
        counter = 0
        for word in words:
            while True:
                user_input = input(color.BOLD +
                                   f"\nEnter {word}: \n" + color.END)
                if user_input.isdigit() or user_input.strip() == "":
                    print(color.BOLD + color.RED +
                          f"Invalid input. Please enter {word}.\n"
                          + color.END)
                elif len(user_input) <= 2:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too short.
                          Please try again.
                          """) + color.END)
                elif len(user_input) >= 20:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too long.
                          Please try again.
                          """) + color.END)
                else:
                    inputs.append(user_input)
                    counter += 1
                    if counter == 5:
                        clear_terminal()
                        counter = 0
                    break
        clear_terminal()
        print(color.BOLD + color.YELLOW +
              "Here is your creation!" + color.END)

        story_six = f"""
        One {inputs[0]} {inputs[1]}, I headed to the beach with my
        {inputs[2]} {inputs[3]}. We packed a {inputs[4]} full of
        snacks, sunscreen, and {inputs[5]} and set off on our adventure.
        As soon as we arrived, we could feel the {inputs[6]} sun
        beating down on us. We quickly unpacked and set up our
        {inputs[4]} and got ready to hit the waves and {inputs[7]}.\n
        But as soon as I jumped in, I realized that the water was
        freezing {inputs[8]}! I swam out to my friends, who were
        {inputs[9]} and having a great time. I decided to
        join in, even though I could barely feel my {inputs[10]}.\n
        As we played in the water, we suddenly heard a loud
        {inputs[11]} coming from the {inputs[12]}. We swam back to
        find a {inputs[13]} crowd of people gathered around a
        {inputs[14]} that had washed up {inputs[15]} on the beach.\n
        Feeling curious, we pushed our way through the crowd to get
        a closer look. As we approached, we could smell the
        {inputs[16]} stench of a dead {inputs[17]}.\n
        Suddenly, a massive {inputs[18]} swooped down and
        started {inputs[19]} on the {inputs[17]}. We all screamed
        and ran away, narrowly avoiding being
        hit hard by the {inputs[18]}.\n
        After that crazy encounter, we decided to pack up
        our {inputs[5]} and head home. As we drove away, we
        couldn't help but laugh at the absurdity of
        our day at the beach.\n\n"""

        typewriter_print(color.BOLD + textwrap.dedent(story_six))
        restart_game()
    # Story Seven

    elif selected_story_title == "My First Day at School":

        words = ['a feeling', 'an adjective, e.g. "pretty"',
                 'an adverb, e.g. quickly', 'a noun, e.g. "dog" or "cup"',
                 'another adjective', 'a plural noun, e.g. "dogs"',
                 'a verb ending in -ing, e.g. "running"',
                 'another verb ending in -ing',
                 'another verb ending in -ing', 'another noun',
                 'another adjective', 'a place, e.g. "park"',
                 'another plural noun', 'another plural noun',
                 'another verb ending in -ing', 'the name of someone you know',
                 'your favourite superhero', 'another plural noun',
                 'another plural noun', 'another adjective']

        inputs = []
        counter = 0
        for word in words:
            while True:
                user_input = input(color.BOLD +
                                   f"\nEnter {word}: \n" + color.END)
                if user_input.isdigit() or user_input.strip() == "":
                    print(color.BOLD + color.RED +
                          f"Invalid input. Please enter {word}.\n"
                          + color.END)
                elif len(user_input) <= 2:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too short.
                          Please try again.
                          """) + color.END)
                elif len(user_input) >= 20:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too long.
                          Please try again.
                          """) + color.END)
                else:
                    inputs.append(user_input)
                    counter += 1
                    if counter == 5:
                        clear_terminal()
                        counter = 0
                    break
        clear_terminal()
        print(color.BOLD + color.YELLOW +
              "Here is your creation!" + color.END)

        story_seven = f"""
        On my first day of school, I felt {inputs[0]} as I walked
        into the classroom. My {inputs[1]} teacher greeted
        me with a big smile and {inputs[2]} showed me to my
        {inputs[3]}. As I sat down, I couldn't help but notice the
        {inputs[4]} students and {inputs[5]} around me. Some were
        {inputs[6]}, while others were {inputs[7]} and {inputs[8]}
        all over the classroom.\n
        Just as the teacher was about to start the lesson, an enormous
        {inputs[9]} burst into the room. It was a {inputs[10]} {inputs[9]}
        who had lost their way to the {inputs[11]}. The teacher quickly
        helped them find their way, and we all had a good laugh about it.\n
        As the day went on, we learned about {inputs[12]} and {inputs[13]}.
        No matter what we were learning, we were always {inputs[14]} and
        having a good time. During recess, I made some new friends called
        {inputs[15]} and {inputs[16]} who showed me their cool {inputs[17]}
        and {inputs[18]}. We played games and laughed so hard that we almost
        forgot we were at school.\n
        As the day came to an end, I felt happy and {inputs[19]}. So if
        you're feeling {inputs[19]} about your first day of school,
        just remember that it's a new adventure full of surprises and
        {inputs[1]} moments.\n\n"""

        typewriter_print(color.BOLD + textwrap.dedent(story_seven))
        restart_game()

    # Story Eight

    elif selected_story_title == "A Wild Party":

        words = ['an adjective, e.g. "pretty"', 'a body part',
                 'another adjective', 'another adjective',
                 'a plural noun, e.g. "dogs"',
                 'a verb ending in -ing, e.g. "running"',
                 'another verb ending in -ing', 'another adjective',
                 'a noun, e.g. "dog" or "table"', 'an adverb, e.g. quickly',
                 'another verb ending in -ing', 'another adjective',
                 'a colour', 'an item of clothing (plural)',
                 'a number, e.g. "fifty seven"', 'another plural noun',
                 'an adverb, e.g. quickly', 'another verb ending in -ing',
                 'another adjective', 'another plural noun']

        inputs = []
        counter = 0
        for word in words:
            while True:
                user_input = input(color.BOLD +
                                   f"\nEnter {word}: \n" + color.END)
                if user_input.isdigit() or user_input.strip() == "":
                    print(color.BOLD + color.RED +
                          f"Invalid input. Please enter {word}.\n"
                          + color.END)
                elif len(user_input) <= 2:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too short.
                          Please try again.
                          """) + color.END)
                elif len(user_input) >= 20:
                    print(color.BOLD + color.RED + textwrap.dedent("""\
                          Your input is too long.
                          Please try again.
                          """) + color.END)
                else:
                    inputs.append(user_input)
                    counter += 1
                    if counter == 5:
                        clear_terminal()
                        counter = 0
                    break
        clear_terminal()
        print(color.BOLD + color.YELLOW +
              "Here is your creation!" + color.END)

        story_eight = f"""
        Last night I went to the craziest party ever. It was so
        {inputs[0]} that my {inputs[1]} is still recovering from it.
        When I arrived, the music was {inputs[2]} and the dance
        floor was packed with {inputs[3]} people and wild {inputs[4]}.
        I started {inputs[5]} to the beat and before I knew
        it, I was {inputs[6]} with a group of {inputs[7]} strangers.\n
        Things really got out of hand when someone suggested we play
        {inputs[8]} pong. I've never been good at that game,
        but I managed to {inputs[9]} {inputs[10]} a few shots and
        impress everyone. As the night went on, more and more
        people and {inputs[4]} showed up.\n
        There were {inputs[11]} characters in crazy costumes,
        some wearing {inputs[12]}{inputs[13]}. I even saw one
        magician trying to juggle {inputs[14]}{inputs[15]} while
        riding a unicycle.\n
        A lot of the night became blurry after that,
        but I found myself {inputs[16]}{inputs[17]} on a couch with a
        {inputs[18]} person who I had never met before. We started
        talking about {inputs[19]} and ended up dancing all night.
        The party didn't really start to wind down until the early
        hours of the morning. It was definitely a night I'll
        never forget!\n\n"""

        typewriter_print(color.BOLD + textwrap.dedent(story_eight))
        restart_game()


def restart_game():
    '''
    Restarts the game if the user wishes to
    Takes the user back to the main page if
    they choose to replay
    Ends the game if the user does not choose
    to replay
    '''
    response = input(color.BOLD + color.GREEN + textwrap.dedent("""\
                     Do you want to play again? Y/N: \n
                     """ + color.END))
    while response.upper() not in ("Y", "N"):
        print(color.BOLD + color.RED +
              "Invalid response. Please enter Y or N.\n" + color.END)
        response = input(color.BOLD + color.GREEN + textwrap.dedent(
                         """\
                         Do you want to play again? Y/N: \n
                         """ + color.END))
    if response.upper() == "Y":
        clear_terminal()
        start_game()
    else:
        clear_terminal()
        print(color.BOLD + color.CYAN + textwrap.dedent("""\
              We're sad to see you go, but we
              hope you had some good laughs!\n
              """ + color.END))
        reply = input(color.BOLD + color.GREEN + textwrap.dedent("""\
                      Would you like to return to
                      the main page? Y/N:\n
                      """
                      + color.END))
        if reply.upper() == "Y":
            clear_terminal()
            start_game()
        else:
            clear_terminal()
            print(color.BOLD + textwrap.dedent("""\
                  Thanks for playing! If you'd like to play again,
                  just click the 'Run Program' button above the terminal
                  to start the game again!""" + color.END))
            sys.exit(0)


if __name__ == "__main__":
    start_game()
    restart_game()
