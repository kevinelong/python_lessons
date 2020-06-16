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

f = open("quiz_form.html", "w")

style = """<style>
        form label {
            display: inline-block;
        }
    </style>

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


    """


f.write(style)

r = 1

for question in Quiz:
    i = 1
    f.write("<fieldset><legend>" + question["q"] + "</legend>")

    for answer in question["answers"]:
        f.write("""<p><label for="g{index}"><input type="radio" name="{g}" id="g{index}" value="{f}"> {a}</label></p>\n""".format(a=answer, g=r, index=i, f=answer[0]))
        i += 1
    f.write("</fieldset>")
    r += 1

f.write("""<input type="submit">
</form>
</body>
</html>""")

   # # ans = raw_input('case sensitive> ')
   #
   #  #if ans == question["correct"]:
   #      f.write("correct")
   #  #else:
   #      f.write("incorrect")

f.close()