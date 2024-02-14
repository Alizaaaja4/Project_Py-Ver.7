import json
from difflib import get_close_matches
from colorama import Fore

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q['question'] == question:
            return q['answer']

def chat_bot():
    header()
    
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    
    while True:
        user_input: str = input (Fore.RED+'You: ')
        
        if user_input.lower() == 'quit':
            break
        
        best_match: str | None = find_best_match(user_input, [q['question'] for q in knowledge_base['questions']])
        
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(Fore.YELLOW+f'Bot: {answer}\n')
        else:
            print(Fore.YELLOW+'Bot: Maaf saya tidak tau tentang itu. Dapatkan kamu memberi tahu saya ?\n')
            new_answer: str = input(Fore.CYAN+"Berikan jawaban untuk BOT ?\n ketik 'skip' untuk melewati ini:  ")
            
            if new_answer.lower() != 'skip':
                knowledge_base['questions'].append({'question': user_input, 'answer': new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print(Fore.YELLOW+'Bot: Terimakasih !! Saya akan mempelajari tentang ini !\n')

def header():
    print(Fore.GREEN+"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-")
    print('|||                   EduQuery ChatBot                   |||')
    print('____________________________________________________________')
    print('|||         Developer by Aliza Nurfitrian [ALL]          |||')
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-")
    
# all function
if __name__ == "__main__":
    chat_bot()
