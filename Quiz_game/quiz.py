import json
import time

Topics_list = ['science','history','technology','gk','commerce']

def one_que(question):
    print('\n' + question)
    choice = input('Enter your choice [a/b/c/d]: ')
    while True:
        if choice.lower() in ['a','b','c','d']:
            return choice
        else:
            print("Invalid choice. please enter again")
            choice = input('Enter Choice [a/b/c/d]: ')


def one_result(key, meta):
    actual = meta['answer']
    if meta['user_response'].lower() == actual.lower():
        print('Q.{} Absolutely Correct!\n'.format(key))
        return 2
    else:
        print('Q.{} Incorrect'.format(key))
        print("Right Answer is ({})".format(actual))
        print('Learn more: ' + meta['more_info'] + "\n")
        return -1

def test(questions):
    score = 0
    print('General Instructions:\n1. Please enter only the choice letter corresponding to the correct answer.\n2. Each question carries 2 points\n3. Wrong answer leads to -1 marks per question\nQuiz will start momentarily. Good Luck!\n')
    time.sleep(10)
    for key, meta in questions.items():
        questions[key]['user_response'] = one_que(meta['question'])
    print("\n================ RESULTS ===================\n")
    for key, meta in questions.items():
        score += one_result(key, meta)
    print("Your Score: ", score,'/', (2 *len(questions)))



def load_question(filename):

    questions = None
    with open(filename, 'r') as read:
        questions = json.load(read)
    return questions

def play_quiz():
    flag = False
    try:
        choice = int(input("Welcome to Today's Quiz!\nChoose your domain of interest:\n(1). Science\n(2). History of India\n(3). Commerce\n(4). Technology\n(5). Gk\nEnter Your Choice [1/2/3/4/5]: "))
        if choice > len(Topics_list) or choice < 1:
            print('Invalid choice. Please enter again')
            flag = True
    except ValueError as e:
        print('Invalid choice, please enter again')
        flag = True
    
    if not flag:
        questions = load_question('topics/'+Topics_list[choice-1]+'.json')
        test(questions)
    else:
        play_quiz()

def user_prompt():
    print('Want to test your GK?\nA. Yes\nB. No')
    play = input()
    if play.lower() == 'a' or play.lower() == 'y':
        play_quiz()
    elif play.lower() == 'b':
        print('Please come back again')
    else:
        print("I don't understand.\nPress A to play, or B to quit.")
        user_prompt()

def execute():
    user_prompt()

if __name__=="__main__":
    execute()