#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk

# Define question dictionaries for each difficulty level
question_data = {
    "Python": {
        "simple": {
             "Which of the following is the correct extension of the Python file?": ['.python', '.pl', '.py', '.p'],
    "All keywords in Python are in _": ['Capitalized', 'lower case', 'UPPER CASE','None of the above'],
    "Which keyword is used for function in Python language?": ['Function', 'def', 'Fun', 'Define'],
    "Which of the following is the correct way to comment in Python?": ['// This is a comment', '# This is a comment', '/* This is a comment */', '-- This is a comment'],
    "How do you print 'Hello, World!' in Python?": ['echo("Hello, World!")', 'print("Hello, World!")', 'printf("Hello, World!")', 'display("Hello, World!")'],
    "What is the purpose of the 'if' statement in Python?": ['To create a loop', 'To define a function', 'To make decisions in code', 'To import modules'],
    "Which data type is used to store a sequence of characters in Python?": ['int', 'float', 'str', 'list'],
    "What does the '%' operator do in Python?": ['Exponentiation', 'Modulo (remainder)', 'Division', 'Multiplication'],
    "How do you declare a variable in Python?": ['var x = 5', 'x = 5', 'int x = 5', 'variable x = 5'],
    "Which of the following is the correct way to create a function in Python?": ['function my_function():', 'def my_function():', 'create my_function():', 'define my_function():'],
    "What is the purpose of the 'len()' function in Python?": ['To get the length of a list or string', 'To define a new variable', 'To perform mathematical operations', 'To print a line of text'],
    "How do you check if a value is NOT equal to another value in Python?": ['!=', '==', '=', '<>'],
    "Which loop is used for iterating over a sequence?": ['for loop', 'while loop', 'until loop', 'loop until'],
    "What is the purpose of the 'else' statement in Python?": ['To start a new block of code', 'To handle exceptions', 'To specify an alternative action', 'To define a function'],
    "What is the output of 'print(3 * 'abc')' in Python?": [9, "'abc'", "'abcabcabc'", "'aabbcc'"],
    "In Python, what is the correct way to represent a single-line comment?": ['// This is a comment', '# This is a comment', '/* This is a comment */', '-- This is a comment'],
    "Which module in Python can be used for regular expression matching?": ['regex', 're', 'regexp', 'matchpy'],
    "What is the purpose of the 'elif' statement in Python?": ['To create a loop', 'To handle exceptions', 'To specify an alternative action', 'To define a function'],
    "Which of the following is used to represent a multi-line comment in Python?": ['/* This is a comment */', '// This is a comment', '# This is a comment', '""" This is a comment """'],
    "What method is used to remove the last element from a list in Python?": ['remove()', 'pop()', 'delete()', 'discard()']
},
        "moderate": {
           "Who developed Python Programming Language?": ['Wick van Rossum', 'Rasmus Lerdorf', 'Guido van Rossum','Niene Stom'],
    "Is Python case sensitive when dealing with identifiers?": ['No', 'Yes', 'Machine dependent'],
    "Which of the following is used to define a block of code in Python language?": ['Indentation', 'Key', 'Brackets'],
    "What is the purpose of the 'with' statement in Python?": ['To create a loop', 'To handle exceptions', 'To specify an alternative action', 'To simplify resource management'],
    "Which of the following statements is true about Python's garbage collection?": ['Python uses manual garbage collection', 'Garbage collection in Python is automatic and managed by the interpreter', 'Python doesn’t have a garbage collection mechanism', 'Garbage collection is only applicable to classes'],
    "How do you open a file named 'example.txt' in read mode in Python?": ['file = open("example.txt", "r")', 'file = open("example.txt", mode="read")', 'file = open("example.txt", mode="r")', 'file = open("example.txt")'],
    "In Python, what does the 'self' keyword represent in a class?": ['It refers to the instance of the class', 'It is used for conditional statements', 'It is a variable for storing data', 'It represents the superclass'],
    "What is the purpose of the 'try' and 'except' blocks in Python?": ['To create a loop', 'To handle exceptions', 'To specify an alternative action', 'To define a function'],
    "Which of the following is a correct way to create a tuple in Python?": ['my_tuple = (1, 2, 3)', 'my_tuple = 1, 2, 3', 'my_tuple = [1, 2, 3]', 'my_tuple = {1, 2, 3}'],
    "What is the difference between 'append()' and 'extend()' methods in Python lists?": ['Both methods are used interchangeably', "'append()' adds an entire list as a single element, while 'extend()' adds elements of a list to another list", "'extend()' adds an entire list as a single element, while 'append()' adds elements of a list to another list", 'There is no difference'],
    "How do you exit a Python script?": ['exit()', 'quit()', 'sys.exit()', 'All of the above'],
    "What is the purpose of the 'lambda' function in Python?": ['To create anonymous functions', 'To define class methods', 'To perform complex mathematical operations', 'To handle exceptions'],
    "What is the output of the expression '3 + 4 * 2' in Python?": [11, 14, 22, 24],
    "Which module in Python is used for working with regular expressions?": ['regex', 're', 'regexp', 'matchpy'],
    "What is the purpose of the 'map()' function in Python?": ['To create a dictionary', 'To apply a function to every item in an iterable', 'To filter elements in a list', 'To concatenate strings'],
    "In Python, what is the purpose of the 'super()' function in a class?": ['To call a method from a superclass', 'To define a class variable', 'To create an instance of a class', 'To access the private members of a class'],
    "What is the output of the code 'print(list(range(1, 5)))' in Python?": ['[1, 2, 3, 4]', '[1, 2, 3, 4, 5]', '[0, 1, 2, 3, 4]', '[0, 1, 2, 3, 4, 5]'],
    "How can you convert a string to a lowercase in Python?": ['string.lower()', 'string.casefold()', 'string.toLower()', 'string.lowercase()'],
    "What does the 'pass' statement do in Python?": ['It raises an exception', 'It continues to the next iteration of a loop', 'It is a placeholder that does nothing', 'It breaks out of a loop']
},
        "difficult": {
    "Which of the following types of loops are not supported in Python?": ['for', 'do while', 'while', 'if'],
    "In which year was the Python language developed?": ['1995', '1972', '1989'],
    "Which of the following is not the part of python programming?": ['Pointers', 'Loops', 'Dynamic typing'],
    "What is the purpose of the 'zip' function in Python?":['Combines two lists into a list of tuples','Counts the number of elements in a list','Reverses the order of elements in a list','Removes duplicates from a list'],
    "In Python, what does the _name_ variable represent?":['The name of the module','The name of the function','The name of the class','The name of the variable'],
    "What is the purpose of the json.dumps() function in Python?":['Loads JSON data','Dumps JSON data to a string','Decodes JSON data','Encodes JSON data'],
    "How do you create an empty set in Python?":['set()','{}','empty_set()','new Set()'],
    "Which of the following is the correct way to import a module named mymodule in Python?":['import mymodule as mm','import module.mymodule','import mymodule','from module import mymodule'],
    "What is the purpose of the _getitem_ method in Python?":['To get an item from a list','To get an item from a dictionary','To get an item from a set','To get an item from an iterable'],
    "How do you remove an item from a list by its value in Python?":['list.remove(value)','list.pop(value)','list.delete(value)','list.discard(value)']
}
,
        "answers": {
            "simple": ['.py', 'None of the above', 'def','# This is a comment','print("Hello, World!")','To make decisions in code','str','Modulo (remainder)','x = 5','def my_function():','To get the length of a list or string','!=','for loop','To specify an alternative action',"'abcabcabc'",'# This is a comment','re','To specify an alternative action', '""" This is a comment """','pop()'],
            "moderate": ['Guido van Rossum', 'Yes', 'Indentation','To simplify resource management','Garbage collection in Python is automatic and managed by the interpreter','file = open("example.txt", mode="r")','It refers to the instance of the class','To handle exceptions','my_tuple = (1, 2, 3)',"'append()' adds an entire list as a single element, while 'extend()' adds elements of a list to another list",'All of the above','To create anonymous functions',11,'re','To apply a function to every item in an iterable','To call a method from a superclass','[1, 2, 3, 4]','string.lower()','It is a placeholder that does nothing'],
            "difficult": ['do while', '1989', 'Pointers','Combines two lists into a list of tuples','The name of the module','Dumps JSON data to a string','set()','import mymodule','To get an item from a list','list.remove(value)'],
        }
    },
    "Java": {
        "simple": {
            "Which of the following is NOT a primitive data type in Java?": ['int', 'boolean', 'string', 'double'],
            "What is the correct syntax for declaring a variable in Java?": ['variable x;', 'x = 5;', 'int x;', 'x = int;'],
            "How do you initialize an array in Java?": ['int arr[] = {1, 2, 3};', 'array arr = [1, 2, 3];', 'int arr() = {1, 2, 3};', 'array arr() = {1, 2, 3};'],
            "What is the default value of the local variables in Java?": ['0', 'null', 'undefined', '1'],
            "Which keyword is used for inheritance in Java?": ['inherit', 'extends', 'inheritance', 'inherits'],
        },
        "moderate": {
            "What is the purpose of the 'static' keyword in Java?": ['To make a variable accessible to all instances of the class', 'To create a constant variable', 'To define a class method', 'To restrict access to a variable'],
            "How do you achieve multiple inheritances in Java?": ['Using interfaces', 'Using the \'extends\' keyword', 'Java does not support multiple inheritances', 'Using the \'implements\' keyword'],
            "What is the purpose of the 'super' keyword in Java?": ['To call a method from the superclass', 'To create an instance of a class', 'To access the private members of a class', 'To define a class variable'],
            "What is the difference between '== and '.equals()' for comparing strings in Java?": ['Both are used interchangeably', '== compares references, while .equals() compares content', '== compares content, while .equals() compares references', 'There is no difference'],
            "What is the purpose of the 'finally' block in a try-catch-finally statement in Java?": ['To catch exceptions', 'To specify an alternative action', 'To create a loop', 'To guarantee the execution of code'],
        },
        "difficult": {
            "Explain the concept of 'polymorphism' in Java.": ['Polymorphism allows objects of different types to be treated as objects of a common type', 'Polymorphism allows objects of the same type to be treated as objects of different types', 'Polymorphism is not supported in Java', 'Polymorphism is a type of exception handling in Java'],
            "What is the purpose of the 'transient' keyword in Java?": ['To indicate that a variable should not be serialized', 'To make a variable accessible to all instances of the class', 'To specify an alternative action', 'To create an immutable class'],
            "How do you implement threads in Java?": ['By extending the Thread class', 'By implementing the Runnable interface', 'Both A and B', 'Java does not support multithreading'],
            "What is the purpose of the 'hashCode()' method in Java?": ['To calculate the hash code of an object', 'To compare two objects for equality', 'To convert an object to a string', 'To define the hash code of a class'],
            "Explain the concept of 'exception chaining' in Java.": ['Exception chaining allows one exception to cause another', 'Exception chaining is not supported in Java', 'Exception chaining is a form of polymorphism', 'Exception chaining is used for loop control in Java'],
        },
        "answers": {
            "simple": ['string', 'int x;', 'int arr[] = {1, 2, 3};', 'undefined', 'extends'],
            "moderate": ['To make a variable accessible to all instances of the class', 'Using interfaces', 'To call a method from the superclass', '== compares references, while .equals() compares content', 'To guarantee the execution of code'],
            "difficult": ['Polymorphism allows objects of different types to be treated as objects of a common type', 'To indicate that a variable should not be serialized', 'Both A and B', 'To calculate the hash code of an object', 'Exception chaining allows one exception to cause another'],
        }
    },
    "C": {
        "simple": {
            "Which of the following is NOT a valid data type in C?": ['float', 'char', 'string', 'boolean'],
            "What is the correct syntax for declaring an integer variable in C?": ['int x;', 'x = 5;', 'integer x;', 'x : int;'],
            "How do you define a constant in C?": ['#define PI 3.14', 'const float PI = 3.14;', 'final float PI = 3.14;', 'constant PI = 3.14;'],
            "What is the purpose of the 'scanf()' function in C?": ['To print output on the console', 'To read input from the console', 'To perform mathematical operations', 'To define a function'],
            "Which operator is used for logical AND in C?": ['&&', 'and', '&', '||'],
        },
        "moderate": {
            "What is the purpose of the 'typedef' keyword in C?": ['To create a new data type name for an existing data type', 'To define a constant variable', 'To create a new function', 'To specify an alternative action'],
            "How do you dynamically allocate memory in C?": ['malloc()', 'new()', 'allocate()', 'memory()'],
            "What is the purpose of the 'struct' keyword in C?": ['To create a structure or record', 'To define a class', 'To create an array', 'To create a loop'],
            "How do you pass an array to a function in C?": ['By reference', 'By value', 'Both A and B', 'Arrays cannot be passed to functions'],
        },
        "difficult": {
            "Explain the concept of 'pointer' in C.": ['A variable that stores the address of another variable', 'A variable that stores a constant value', 'A variable that points to the end of an array', 'A variable used for exception handling'],
            "What is the purpose of the 'volatile' keyword in C?": ['To indicate that a variable\'s value may change at any time', 'To make a variable constant', 'To create a volatile function', 'To specify an alternative action'],
            "How do you implement a linked list in C?": ['Using pointers', 'Using arrays', 'Using structures', 'Linked lists are not supported in C'],
            "What is the purpose of the 'static' keyword for a function in C?": ['To make the function accessible only within the same file', 'To make the function global', 'To indicate a constant function', 'To create a recursive function'],
            "Explain the concept of 'file handling' in C.": ['Reading from and writing to files', 'Handling exceptions related to files', 'Creating and deleting files', 'File handling is not supported in C'],
        },
        "answers": {
            "simple": ['boolean', 'int x;', '#define PI 3.14', 'To read input from the console', '&&'],
            "moderate": ['To create a new data type name for an existing data type', 'malloc()', 'To create a structure or record', 'By reference'],
            "difficult": ['A variable that stores the address of another variable', 'To indicate that a variable\'s value may change at any time', 'Using pointers', 'To make the function accessible only within the same file', 'Reading from and writing to files'],
        }
    }
}

def start_quiz(language, level):
    global questions, correct_answers, current_question
    questions = question_data[language][level]
    correct_answers = question_data[language]['answers'][level]
    current_question = 0
    start_quiz_questions()

def start_quiz_questions():
    homepage_frame.pack_forget()
    start_button.pack_forget()
    next_button.pack()
    next_question()

def next_question():
    global current_question
    if current_question < len(questions):
        check_ans()
        user_ans.set('None')
        c_question = list(questions.keys())[current_question]
        clear_frame()
        Label(f1, text=f"Question : {c_question}", padx=15, font=("Arial", 15, "bold")).pack(anchor=NW)
        for option in questions[c_question]:
            Radiobutton(f1, text=option, variable=user_ans, value=option, font=("Arial", 15), padx=28).pack(anchor=NW)
        current_question += 1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        output = f"Your Score is {user_score.get()} out of {len(questions)}"
        Label(f1, text=output, font=("Arial", 25, "bold")).pack()
        if user_score.get() < len(questions):
            Label(f1, text="Correct Answers:", font=("Arial", 18, "bold")).pack()
            show_correct_answers()
        Label(f1, text="\n\nThanks for Participating", font=("Arial", 18)).pack()

def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None':
        if temp_ans == correct_answers[current_question - 1]:
            user_score.set(user_score.get() + 1)
        else:
            incorrect_answers.append((list(questions.keys())[current_question - 1], correct_answers[current_question - 1]))

def show_correct_answers():
    for question, correct_answer in incorrect_answers:
        Label(f1, text=f"{question}: {correct_answer}", font=("Arial", 15)).pack()

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

def select_level(language):
    clear_frame()
    Label(f1, text=f"You selected: {language}", padx=15, font=("Arial", 12, "bold")).pack()
    Label(f1, text="Choose level", font=("Arial", 15), padx=15, pady=20).pack()

    level_frame = Frame(f1)
    level_frame.pack()

    level_button = Button(level_frame, text="Simple", command=lambda: start_quiz(language, 'simple'),
                          font=("Arial", 15), bg="purple", fg="white", padx=20)
    level_button.grid(row=0, column=0, padx=10, pady=5)
    level_button = Button(level_frame, text="Moderate", command=lambda: start_quiz(language, 'moderate'),
                          font=("Arial", 15), bg="purple", fg="white", padx=20)
    level_button.grid(row=0, column=1, padx=10, pady=5)
    level_button = Button(level_frame, text="Hard", command=lambda: start_quiz(language, 'difficult'),
                          font=("Arial", 15), bg="purple", fg="white", padx=20)
    level_button.grid(row=0, column=2, padx=10, pady=5)

def submit_choice(selected_language):
    global incorrect_answers
    incorrect_answers = []
    clear_frame()
    Label(f1, text=f"You selected: {selected_language}", padx=15, font=("Arial", 12, "bold")).pack()
    select_level(selected_language)
    
    

if __name__ == "__main__":
    root = Tk()
    root.title("QUIZ APP")
    root.geometry("850x520")
    root.minsize(800, 400)
    root.configure(bg="#E6E6FA")

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    incorrect_answers = []

    Label(root, text="Quiz App", font=("Arial", 40, "bold"), background="purple", fg="white", padx=900, pady=9).pack()
    Label(root, text="", font=("Arial", 10)).pack()

    homepage_frame = Frame(root)
    homepage_frame.pack(side=TOP, fill=X, pady=20)

    style = ttk.Style()
    style.configure('TButton', font=('Arial', 15), padding=10, background='violet')

    submit_button = ttk.Button(homepage_frame, text="Python", command=lambda: submit_choice("Python"), style='TButton')
    submit_button.grid(row=0, column=0, padx=180)
    submit_button = ttk.Button(homepage_frame, text="Java", command=lambda: submit_choice("Java"), style='TButton')
    submit_button.grid(row=0, column=1, padx=180)
    submit_button = ttk.Button(homepage_frame, text="C", command=lambda: submit_choice("C"), style='TButton')
    submit_button.grid(row=0, column=2, padx=180)

    for button in homepage_frame.winfo_children():
        style.configure(str(button), foreground='violet')

    start_button = Button(root, text="Start Quiz", command=start_quiz_questions, font=("Arial", 20), padx=10, pady=3)
    next_button = Button(root, text="Next Question", command=next_question, font=("Arial", 17))

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    root.mainloop()


# In[ ]:




