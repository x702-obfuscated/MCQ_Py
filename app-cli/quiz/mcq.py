import random


from utils.utils import *
from utils.ui import Menu_Option

class MCQ():

    def __init__(self, question, answer, *choices):
        self.question: str = question
        self.answer: str = answer
        self.choices: list[str] = list(choices)
        

        self.prompt = ""
        self.response:str = None

        self.randomize()
        self.options = self.map_choices()

    def __eq__(self, other):
        if isinstance(other, MCQ):
            return self.question == other.question
        return False
    
    def randomize(self) -> None:
        self.choices.append(self.answer)
        random.shuffle(self.choices)

    def check_answer(self,response) -> bool:

        if(self.answer == response):
            print("[\u2705 CORRECT! \u2705]")
            return True
        else:
            print("[\u274C INCORRECT. \u274C]")
            return False
         
    def map_choices(self)-> dict[str:str]:
        
        choice_map: dict[str:str] = {}
        
        for i, e in enumerate(self.choices):
            choice_map[chr(i+65)] = Menu_Option(e)

        return choice_map












    # def make_prompt(self,header,number,footer) -> None:
    #     self.prompt = f"{header}{number}.) {self.question}\n\n"
        
    #     separator = "-" * int(len(header)/2)

    #     self.prompt += separator + "\n"

    #     for key, value in self.choice_map.items():
    #         self.prompt+= (f"{key}: {value}\n")

    #     self.prompt += separator + "\n"

    #     self.prompt += footer


         
    # def get_choice(self) -> str:
    #     length = len(self.choices)
    #     pattern = f"^[a-{chr(length+97)}qrA-{chr(length+65)}QR]" + r"{1}$"

    #     user_in = check_input(
    #         pattern,
    #         self.prompt,
    #         f"Please type only single character from A-{chr(length+65)}",
    #     )

    #     return user_in
    
    # def set_number(self,n)-> None:
    #     self.num_str = str(n) +".) "




    




 






