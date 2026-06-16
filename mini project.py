class Quiz:
    def __init__(self):
        self.score=0
        self.question=[
            {
                "Question":"Which of the following is immutable?",
                "options":["A.Tuple","B.Set","c.Dictionary","D.List"],
                "answer":"A. Tuple"
            },
            {
                "Question":"Which data type is used to store text in Python?",
                "options":["A. int","B. float","C. str","D. bool"],
                "answer":"C. str"
            },
            {
                "Question":"Which function is used to take input from the user?",
                "options":["A. print()","B. input()","C. scan()","D. get()"],
                "answer":"B. input()"
            },
            {
                "Question":"Which keyword is used to define a function in Python?",
                "options":["A. function","B. define","C. func","D. def"],
                "answer":"D. def"
            },
            {
                "Question":"Which collection type is enclosed in square brackets []?",
                "options":["A.Tuple","B.Set","c.Dictionary","D.List"],
                "answer":"D. List"
            }
        ]
    def start_quiz(self):
        print("========Python Quiz=========")
        for i in self.question:
            print("\n"+i["Question"])
            for options in i["options"]:
                print(options)
            while True:
                answer=input("Enter Answer(A/B/C/D):").upper()
                if answer in ("A","B","C","D"):
                    break
                print("Invalid Choice!")
            if answer==i["answer"][0]:
                print("Correct Answer!")
                self.score+=1
            else:
                print("Incorrect Answer!")
                print("correct answer:",i["answer"])
    def show_quiz(self):
        total=len(self.question)
        percentage=(self.score/total)*100
        print("Total marks:",self.score)
        print("percentage:",percentage)
        if percentage>=80:
            print("grade:A")
        elif percentage>=60:
            print("Grade:B")
        elif percentage>=40:
            print("Grade:c")
        else:
            print("fail")
quiz=Quiz()
quiz.start_quiz()
quiz.show_quiz()

