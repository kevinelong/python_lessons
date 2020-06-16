
Quiz = [
    {"q": "Which of these is not a fruit?",
     "answers": ['Banana', 'Strawberry', 'Tomato', 'Apple'],
     "correct": 'Strawberry'
    },



    {"q": "Is Portland Weird?",
     "answers": ['Yes', 'No'],
     "correct": 'Yes'
    }
]



f = open("Quiz_form.html", "w")


f.write("""
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        form label {
            display: inline-block;
        }
    </style>
</head>
<body>

<h1>Quiz</h1>

<form method="post" action="evaluate.py">
    <fieldset>
        <legend>When and Who:</legend>
        <label>
            <h2>Date</h2>
            <input name="date_taken" type="date"><br/>
        </label>
        <label>
            <h2>Student Name</h2>
            <input name="student_name_first" placeholder="first">
            <input name="student_name_last" placeholder="last">
        </label>
    </fieldset>

    <hr>

""")


f.write("""<form method="post" action="evaluate.py">""")
question_index = 1
for question in Quiz:
    f.write("""
        <fieldset>
        <legend>%s:</legend>""" %(question["q"]))


    for answer in question["answers"]:
        f.write("""
        <p><label for="g%d"><input type="radio" name="g%d" id="g%d" value="%d"> %s</label></p>

        """ %(question_index, question_index, question_index, question_index, answer))
    question_index = question_index + 1

    f.write("""</fieldset>
    """)

f.write("""
    <input type="submit">
    </form>
    </body>
    </html>""")
f.close()











