import requests, re, random

wordlist = requests.get("https://meaningpedia.com/5-letter-words?show=all")

pattern = re.compile(r'<span itemprop="name">(\w+)</span>')

word_list = pattern.findall(wordlist.text)

word = random.choice(word_list)

lives = 6
guesslist = ["_","_","_","_","_"]
guess = ''

running = True

while running:
    correctletters = []
    correctloc = []
    corloc=''
    corlet=''
    if len(guess) == 5:
        if guess in word_list:
            for i in range(len(guess)):
                if guess[i] in word:
                    if guess[i] == word[i]:
                        correctloc.append(guess[i])
                    else:
                        correctletters.append(guess[i])
            lives -= 1
            for i in correctloc:
                corloc += i
                corloc += ", "
            for i in correctletters:
                corlet += i
                corlet += ", "
            print(f'''
        Correct letters (with correct location): {corloc}
        Letters in the word, but in the wrong location: {corlet}
        Lives left: {lives}
        ''')
            if guess == word:
                input("Congratulations! You got it right!")
                running = False
                break

            elif lives == 0:
                input(f"Out of lives! You Lost! The correct word was {word}")
                running = False
                break
            guess = ''
        else:
            print("No such word found.")
            guess = input("Enter your guess:")
    else:
        print("Please only input 5 lettered words.")
        guess = input("Enter your guess:")