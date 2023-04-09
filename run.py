# Welcome message

# Instructions

# Story Title Selection 

# Define the list of story titles

story_titles = ["A Peculiar Adventure", "A Strange Fairytale", "A Day at the Office", 
                "One Summer Vacation", "A Scary Encounter", "A Day at the Beach", 
                "My First Day at School", "A Wild Party"]

# Print the list of story titles for the user to see
print("Please select a story by entering the corresponding number:")
for i, title in enumerate(story_titles):
    print(f"{i+1}. {title}")

# Ask the user to select a story
selected_story_index = int(input("Enter the number of the story you'd like to read: ")) - 1

# Retrieve the selected story title
selected_story_title = story_titles[selected_story_index]

# Print the selected story title for the user to see
print(f"You have selected the story: {selected_story_title}")

# Mad Libs One of Eight

# User inputs One of Eight: Status: DONE ALL 20

if selected_story_title == "A Peculiar Adventure": 

    adjective_one = input("Enter an adjective: ")
    feeling_one = input("Enter a feeling: ")
    noun_one = input("Enter a noun: ")
    place_one = input("Enter a place: ")
    adjective_two = input("Enter another adjective: ")
    animal_one = input("Enter a type of animal: ")
    noun_two = input("Enter another noun: ")
    adjective_three = input("Enter another adjective: ")
    verb_one = input("Enter a verb ending in -ed: ")
    plural_noun_one = input("Enter a plural noun: ")
    adjective_four = input("Enter another adjective: ")
    adverb_one = input("Enter an adverb: ")
    feeling_two = input("Enter another feeling: ")
    noun_three = input("Enter another noun: ")
    noun_four = input("Enter another noun: ")
    feeling_three = input("Enter another feeling: ")
    number_one = input("Enter a random number: ")
    adjective_five = input("Enter another adjective: ")
    feeling_four = input("Enter another feeling: ")
    verb_two = input("Enter a verb in the present tense: ")

# Story Template One of Eight

    story_one = f"""One {adjective_one} day, I woke up feeling {feeling_one}
    and decided to go on a crazy adventure. I grabbed my trusty {noun_one} and
    set off into the {place_one} wilderness. As I walked, I came across a {adjective_two}
    {animal_one} who asked me for help. 'I've lost my {noun_two}!' they exclaimed. Being
    the {adjective_three} person I am, I offered to help. We {verb_one} high and
    low, through dense forests and mysterious {plural_noun_one}, until finally we found the
    missing {noun_two}. The {noun_two} was so {adjective_four} that we couldn't resist taking
    a selfie {adverb_one} with it. Feeling {feeling_two}, I said goodbye to my new friend, {animal_one},
    and continued on my wild adventure.

    Soon, I stumbled upon a giant {noun_three} who challenged me
    to a {noun_four} contest. I was feeling {feeling_three}, so I accepted. We went back and forth,
    with each of us throwing {number_one} punches at each other back and forth. In the end, I emerged
    victorious, much to the {adjective_five} disappointment of my opponent. Exhausted but {feeling_four},
    I returned home and went straight to bed.

    As I drifted off to {verb_two}, I couldn't help but think
    that it had been a truly remarkable day. So if you're feeling {feeling_one} and in need of an adventure,
    grab your {noun_one} and set off into the {adjective_four} unknown. Who knows what kind of
    {adjective_three} and {adjective_two} things you might find along the way!"""

    print(story_one)

# User inputs Two of Eight

elif selected_story_title == "A Strange Fairytale": 

    adjective_one = input("Enter an adjective: ")
    noun_one = input("Enter a noun: ")
    verb_one = input("Enter a verb ending in -ing: ")
    verb_two = input("Enter another verb: ")
    place_one = input("Enter a place: ")
    adjective_two = input("Enter another adjective: ")
    noun_two = input("Enter another noun: ")
    verb_three = input("Enter another verb: ")
    adjective_three = input("Enter another adjective: ")
    noun_three = input("Enter another noun: ")
    exclamation = input("Enter an exclamation, e.g. 'OMG!' or 'Wow!' or 'Oh no!': ")
    adjective_four = input("Enter another adjective: ")
    verb_four = input("Enter a verb in the past tense: ")
    verb_five = input("Enter another verb ending in -ing: ")
    adverb_one = input("Enter an adverb: ")
    noun_four = input("Enter another noun: ")
    verb_six = input("Enter another verb in the past tense: ")
    random_date = input("Enter a random date, e.g. 1995: ")
    any_number = input("Enter a random number: ")

# Story Template Two of Eight

    story_two = f"""Once upon a time, in a land far, far away, there was a {adjective_one} {noun_one} who 
    loved to {verb_one}. One day, while {verb_two + 'ing'} in the {place_one}, the {adjective_one} {noun_one} 
    stumbled upon a {adjective_two} {noun_two} who was {verb_three + 'ing'} with a {adjective_three} {noun_three}.
    "Hey there, {exclamation}!" exclaimed the {adjective_one} {noun_one}. "Would you like to join us in our 
    {adjective_four} {verb_one + 'ing'}?"

    Without hesitation, the {adjective_two} {noun_two} agreed and soon found themselves {verb_one + 'ing'} 
    with the {adjective_two} {noun_two} and their {adjective_three} {noun_three}. They {verb_four} and {verb_four}, 
    and even did a little {verb_five} together.

    But then, out of nowhere, a {adjective_four} {noun_four} appeared and started throwing things {adverb_one} at them! 
    The {adjective_one} {noun_one} and the {adjective_two} {noun_two} were afraid, but to their surprise, the 
    {adjective_three} {noun_three} stood tall and {verb_six} the {adjective_four} {noun_four}.
    From {random_date}, the {adjective_one} {noun_one} made a promise to themselves to always be open to new experiences 
    and never to be afraid of a little {verb_one}. And who knows? Maybe they'll even meet another {any_number} 
    {adjective_four} {noun_four} along the way.
    The end."""

    print(story_two)

# User inputs Three of Eight

# Story Template Three of Eight

elif selected_story_title == "A Day at the Office":

    feeling_one = input("Enter a feeling: ")
    city_one = input("Enter the name of a city: ")
    noun_one = input("Enter a noun: ")
    noun_two = input("Enter another noun: ")
    adjective_one = input("Enter an adjective: ")
    feeling_two = input("Enter a feeling: ")
    verb_one = input("Enter a verb: ")
    noun_three = input("Enter a noun: ")
    verb_two = input("Enter another verb: ")
    any_number = input("Enter a random number: ")
    adjective_two = input("Enter another adjective: ")
    city_two = input("Enter another name of a city: ")
    adverb_one = input("Enter an adverb: ")
    adjective_three = input("Enter another adjective: ")
    noun_four = input("Enter another noun: ")
    adjective_four = input("Enter another adjective: ")
    plural_noun_one = input("Enter a plural noun: ")
    feeling_three = input("Enter another feeling: ")
    noun_three = input("Enter another noun: ")
    clothing_plural = input("Enter an item of clothing (plural): ")

    story_three = f'''It was just another {1. feeling_one} day in the office in {2. city_one} when I arrived at my 
    large {3. noun_one}. I sat down at my {3. noun_one} and opened up my {4. noun_two} to start my {5. adjective_one} work. 
    But before I could even begin, my {6. feeling_two} coworker walked in and started {7. verb_one + 'ing'} loudly 
    about their {8. noun_three} problems. I tried to tune them out, but their voice was so annoying that I couldn't {9. verb_two}.
    
    After what felt like {10. Any number} hours of their constant {7. verb_one + 'ing'}, I decided to take a {11. adjective_two} 
    break and visit the office in {12. city_two}.As I walked {13. adverb_one} down the hallway, I noticed a {14. adjective_three} 
    smell coming from the break room. I cautiously peeked inside, and to my horror, I saw that someone had left their {15. noun_four} 
    in the microwave for way too long.
    
    The {15. noun_four} was now a {16. adjective_four} mess, and the entire room smelled like burnt {17. plural_noun_four}.
    Feeling {18. feeling_three}, I quickly made my way back to my {3. noun_one}, only to find that my {4. noun_two} had 
    mysteriously disappeared! After a few minutes of searching {19. adverb_one}, I finally found it hiding under a pile of 
    dirty {20. Piece of clothing(plural)}.
    
    So if you're ever feeling bored at work, just remember to keep your eyes and ears open for any weird moments that might come your way.
    You never know what kind of {15. noun_three} might be waiting just around the corner in {2. city_one}!'''

# User inputs One of Eight

# Mad Libs One of Eight
# Story Template One of Eight
# User inputs One of Eight

# Mad Libs One of Eight
# Story Template One of Eight
# User inputs One of Eight

# Mad Libs One of Eight
# Story Template One of Eight
# User inputs One of Eight

# Mad Libs One of Eight
# Story Template One of Eight
# User inputs One of Eight



