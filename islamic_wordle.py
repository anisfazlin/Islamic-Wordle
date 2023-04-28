import enum
from tkinter import *
from tkinter import messagebox
import random 

# dictionary of Islamic terms (46 terms + meaning)
word_list = {
    'AHZAB': 'Refers to the battles fought by the Prophet Muhammad and his companions.', 
    'ALLAH': 'The Arabic word for God in Islam.', 
    'AURAH': 'Refers to the parts of the body that should be covered according to Islamic dress code.', 
    'BATIL': 'Refers to falsehood or invalidity in Islamic law.', 
    'BATIN': 'The inner, spiritual dimension of Islam.', 
    'BURQA': 'A garment worn by some Muslim women to cover their entire body and face.', 
    'DUNYA': 'Refers to the material world or worldly concerns in Islam.', 
    'FAQIH': 'An Islamic scholar who specializes in Islamic law.', 
    'FARDU': 'Refers to actions that are mandatory in Islam.', 
    'FATWA': 'A legal opinion or ruling issued by an Islamic scholar.', 
    'FITRA': 'Refers to the natural disposition towards belief in God in Islam.', 
    'GHAZI': 'Refers to a Muslim warrior who has participated in a battle.', 
    'HAFIZ': 'A person who has memorized the entire Quran.', 
    'HALAL': 'Refers to food, drink, or actions that are permissible according to Islamic law.', 
    'HARAM': 'Refers to food, drink, or actions that are forbidden according to Islamic law', 
    'HIJAB': ' The headscarf worn by Muslim women.', 
    'IFTAR': 'The meal eaten by Muslims after sunset during the month of Ramadan.', 
    'IHRAM': 'The state of ritual purity required for performing the Hajj or Umrah pilgrimage.', 
    'IHSAN': 'The concept of doing good and behaving excellently towards others.', 
    'INJIL': 'The Arabic word for the Gospels of Jesus, which are considered a holy text in Islam.', 
    'ISLAM': 'The name of the religion based on the teachings of the Prophet Muhammad.', 
    'JIHAD': 'A struggle or striving for the sake of Allah and can refer to an individual inner struggle to do good or a physical struggle to defend Islam.', 
    'KAFIR': 'A term used to describe non-Muslims', 
    'KITAB': 'The Arabic word for book, often used to refer to the Quran.', 
    'NIKAH': 'The Islamic marriage ceremony.', 
    'QADAR': 'The Islamic belief in fate and divine predestination.', 
    'QIBLA': 'The direction that Muslims face during prayer, which is towards the Kaaba in the city of Mecca.', 
    'RAKAT': 'The unit of prayer in Islam, which consists of a sequence of standing, bowing, and prostrating', 
    'RASUL': 'A messenger of Allah, specifically referring to prophets in Islam.', 
    'SALAM': 'A common greeting in Arabic, which also means "peace".', 
    'SHIRK': 'The sin of associating partners with Allah in worship.', 
    'SOLAT': 'The Arabic word for prayer in Islam.', 
    'SOLEH': 'A person who is pious and righteous.', 
    'SUJUD': 'The act of prostration during Islamic prayer.', 
    'SUNNI': 'The largest branch of Islam, This term comes from the word "Ahl al-Sunnah wal-Jamaah", which means "People of the Sunnah and the Community', 
    'SURAH': 'A chapter in the Quran.', 
    'TALAQ': 'The Islamic form of divorce.', 
    'TAQWA': 'The concept of being conscious and mindful of Allah in all aspects of life.', 
    'TAWAF': 'The act of circumambulating the Kaaba during the Hajj or Umrah pilgrimage.', 
    'UMRAH': 'A pilgrimage to Mecca that can be undertaken at any time of the year', 
    'USRAH': 'A term used in Islamic societies to refer to a small group or circle of friends who meet regularly to discuss and learn more about Islam together. It derived from Arabic term meaning "family"', 
    'WAJIB': 'Refers to actions that are obligatory', 
    'WUDHU': 'The Islamic ablution ritual, which involves washing specific parts of the body before prayer.', 
    'ZAKAT': 'An obligatory charity given by Muslims, usually in the form of a percentage of their wealth.'
}

root = Tk()
root.title('Islamic Wordle')
word = random.choice(list(word_list.keys()))

GREEN = '#007d21'
YELLOW = '#e2e600'
BLACK = '#000000'
WHITE = '#FFFFFF'

root.config(bg=BLACK)

guessnum = 0

wordInput = Entry(root)
wordInput.grid(row=999, column=0, padx=20, pady=20, columnspan=5)

# To insert the string dictionary to avl tree
def insert(root, key, value):
    if root is None:
        return {'key': key, 'value': value, 'height': 1, 'left': None, 'right': None}
    elif key < root['key']:
        root['left'] = insert(root['left'], key, value)
    elif key > root['key']:
        root['right'] = insert(root['right'], key, value)
    else:
        root['value'] = value

    root['height'] = 1 + max(get_height(root['left']), get_height(root['right']))
    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and key < root['left']['key']:
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and key > root['right']['key']:
        return left_rotate(root)

    # Left Right Case
    if balance > 1 and key > root['left']['key']:
        root['left'] = left_rotate(root['left'])
        return right_rotate(root)

    # Right Left Case
    if balance < -1 and key < root['right']['key']:
        root['right'] = right_rotate(root['right'])
        return left_rotate(root)

    return root

#to left rotate the tree
def left_rotate(z):
    y = z['right']
    T2 = y['left']

    y['left'] = z
    z['right'] = T2

    z['height'] = 1 + max(get_height(z['left']), get_height(z['right']))
    y['height'] = 1 + max(get_height(y['left']), get_height(y['right']))

    return y

#to right rotate the tree
def right_rotate(z):
    y = z['left']
    T3 = y['right']

    y['right'] = z
    z['left'] = T3

    z['height'] = 1 + max(get_height(z['left']), get_height(z['right']))
    y['height'] = 1 + max(get_height(y['left']), get_height(y['right']))

    return y

#to get the height of the tree
def get_height(root):
    if root is None:
        return 0
    return root['height']

#to balance the tree
def get_balance(root):
    if root is None:
        return 0
    return get_height(root['left']) - get_height(root['right'])


def create_avl_tree(word_list):
    root = None
    for key, value in word_list.items():
        root = insert(root, key, value)
    return root

#To create avl tree
avl_tree = create_avl_tree(word_list)

#this function is to get the value(meaning) of the key(islamic term) in the tree 
def get_value(root, key):
    if root is None:
        return None
    elif root['key'] == key:
        return root['value']
    elif key < root['key']:
        return get_value(root['left'], key)
    else:
        return get_value(root['right'], key)

#breadth first search to check whether the guess is existed in the tree
def breadth_first_search(root, target):
    if root is None:
        return None

    queue = [root]

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node['key'] == target:
            return current_node
        if current_node['left'] is not None:
            queue.append(current_node['left'])
        if current_node['right'] is not None:
            queue.append(current_node['right'])

    return None

def win_lose(winner):
    global guessnum
    if winner == False:
        title = 'You Lose'
        message = f'The word was {word}'
    else:
        title = 'You Win'
        message = f'Well done, you got it in {guessnum} / 6 guess(s)'
        
    messagebox.showinfo(title=title, message=f'{message}.')
    root.destroy()
    quit()
    
def getGuess():
    global winner
    global word
    guess = wordInput.get().upper()

    global guessnum
    
    guessnum += 1

    if guessnum <= 6:
        
        if len(guess) == 5:

            if word == guess: #CORRECT
                winner = True
                
            else:             #INCORRECT
                for i, letter in enumerate(guess):

                    label = Label(root, text=letter.upper())
                    label.grid(row=guessnum, column=i, padx=10, pady=10)

                    if letter == word[i]: #if they get the letter right
                        label.config(bg=GREEN, fg=BLACK)

                    if letter in word and not letter == word[i]: #if the letter is in the word, but not in the right spot
                        label.config(bg=YELLOW, fg=BLACK)
                    
                    if letter not in word:
                        label.config(bg=BLACK, fg=WHITE)
                if guess not in word_list:
                    messagebox.showerror("Invalid guess", "Please enter an existing Islamic term in your guess.")
        else:
            messagebox.showerror("please use 5 characters", "Please use 5 characters in your guess")
        
        if guessnum == 5:
            messagebox.showinfo("hint", "Hint for the word: " + get_value(avl_tree, word))
    else:
        winner = False
        
    wordInput.delete(0, END)
    win_lose(winner)
       
wordGuessButton = Button(root, text="Guess", command=getGuess)
wordGuessButton.grid(row=999, column=3, columnspan=2)
root.mainloop()