'''
Source of madlib story
https://irp-cdn.multiscreensite.com/ec2b0ab8/files/uploaded/Mad%20Libs.pdf 
'''

"""Madlib Blanks"""


def zooStory():
    adj1 = input("Adjective: ")
    noun = input("Noun: ")
    verbPastTense = input("Verb past tense: ")
    adverb1 = input("Adverb: ")
    adj2 = input("Adjective: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    adj4 = input("Adjective: ")
    verb = input("Verb: ")
    adverb2 = input("Adverb: ")
    verbPastTense2 = input("Verb past tense: ")
    adj5 = input("Adjective: ")

    madlib = f"Today I went to the zoo. I saw a(n) {adj1} {noun} jumping up and \
down in its tree. He {verbPastTense} {adverb1} through the large tunnel \
that led to its {adj2} {noun2}. I got some peanuts and passed them through \
the cage to a gigantic gray {noun3} towering above my head. Feeding that \
animal made me hungry. I went to get a {adj4} scoop of ice cream. It \
filled my stomach. Afterwards I had to {verb} {adverb2} to catch our bus. \
When I got home I {verbPastTense2} my mom for a {adj5} day at the zoo."

    print("=== A Day at the Zoo! ===")
    print(madlib)


def firstDayOfSchool():
    noun1 = input("Noun: ")
    adj1 = input("Adjective: ")
    number1 = input("Number: ")
    adj2 = input("Adjective: ")
    noun2 = input("Noun: ")
    properNoun1 = input("Proper noun: ")
    properNoun2 = input("Proper noun: ")
    pluralNoun1 = input("Plural noun: ")
    ingVerb = input("Verb that ends in 'ing': ")
    pluralNoun2 = input("Plural noun: ")
    adj3 = input("Adjective: ")
    adv1 = input("Adverb: ")

    madlib = f" One very nice morning near the end of summer, my mother \
woke me up at 4:00AM and said, \"Wake up and smell the grass, sleepy \
head! Today is your first day of school and you can't be late.\" I groaned \
in my bed for twenty seconds, but eventually I got dressed. I wore a blue \
and white striped, long sleeve {noun1} with a collar on it, a red tie, \
dark gray pants, white socks, black shoes, and a(n) {adj1} hat. \
In 10 minutes I made lunch and ate my breakfast. {number1} minutes later, \
the bus came. A few minutes later, I was at school.\
\n    In school, I met two really {adj2} kids. All of us became friends \
very fast. THat day we had Science, and luckily my friends and I were \
at the same {noun2}. My friends' names are {properNoun1} and {properNoun2}. \
In Math we weren't together, and that really bugged me. We learned what \
{pluralNoun1} were, and when to use them. At snack and recess, we played \
a game together. It was extremely fun. At PE, we were {ingVerb} off the \
ropes onto {pluralNoun2}. I thought it was a very {adj3} idea. In \
swimming class, we needed to swim extremely {adv1}, or else we would \
have to swim longer.\
\n   Before I knew it, school was over. I grabbed all my belongings \
and put them into my backpack. In two minutes, the bus came. As I \
stepped into the bus I shouted, \"Goodbye, adios amigos, and shalom,\" \
to my friends. Then I went into the bus. In a flash, I was back home. \
This day was an extremely exciting day!"
   
    print("=== A Day at the School! ===")
    print(madlib)

story = input("Do you want story 1 or 2 (1 or 2)?")
match story:
   case "1": zooStory()
   case "2": firstDayOfSchool()
   case other:
      print("I don't know what you mean. Try again.")