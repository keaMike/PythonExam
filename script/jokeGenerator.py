joke_gen = (joke for joke in open('jokes.txt'))

def generate_joke():
    try:
         print(next(joke_gen))
    except StopIteration:
        print('Sorry... No more jokes :(')

while (True):
    answer = input('Wanna hear a joke? Y/n ')

    if answer.lower() == 'y':
        generate_joke()
    else: 
        break
    
