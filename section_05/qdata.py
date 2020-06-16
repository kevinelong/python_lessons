quiz_list = [
    [
        "1. Which of the following is a fruit?",
        [
            "Banana",
            "Strawberry"
        ],
        "Strawberry"
    ],
    [
        "2. Which of the following is a fruit?",
        [
            "Banana",
            "Strawberry"
        ],
        "Strawberry"
    ]
]

def print_all_list():
    for q in quiz_list:
        print(q[0])
        for a in q[1]:
            print(a)
        print("correct = " + q[2])


quiz_dict = {
    "author": "Kevin",
    "questions": [
        {
            "id": 1001,
            "text": "Which of the following is a fruit?",
            "answers": [
                {
                    "code": "A",
                    "text": "Banana",
                    "correct": False
                },
                {
                    "code": "B",
                    "text": "Strawberry",
                    "correct": True
                },
                {
                    "code": "C",
                    "text": "Tomato",
                    "correct": False
                },
                {
                    "code": "D",
                    "text": "Apple",
                    "correct": False
                }
            ],
            "correct": [
                "A",
                "B"
            ]
        },
        {
            "id": 1002,
            "text": "Is Portland weird?",
            "answers": [
                {
                    "code": "A",
                    "text": "Yes",
                    "correct" : True
                },
                {
                    "code": "B",
                    "text": "No",
                    "correct": False
                }
            ],
            "correct": [
                "B"
            ]
        }
    ]
}

def print_all_dict():
    for q in quiz_dict["questions"]:
        print(q["text"])
        for a in q["answers"]:
            if(a["correct"]):
                print(a["code"] + " " + a["text"] + " <-- Correct")
            else:
                print(a["code"] + " " + a["text"])


def is_correct_dict(question, user_answer):
    for a in question["answers"]:
        if a["correct"]:
            if a["text"] == user_answer:
                return True
    return False

print_all_dict()

print(is_correct_dict(quiz_dict["questions"][0], "Banana"))

print(is_correct_dict(quiz_dict["questions"][1], "Yes"))
