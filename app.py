#This code is to demonstrate the multiple dropdown submenus having dynamic contents.

from flask import Flask, render_template, request, url_for

app=Flask(__name__)
courses={
    'java':{
        'course_names': ['core java', 'Intermediate java', 'adv java','The Complete Java Masterclass','Java In-Depth by Udemy','Java Fundamentals by Pluralsight','crash course in Java' ],
        'total_durations': 35,
    } ,
    'python':{
        'course_names':['core python', 'Intermediate python', 'adv python', 'Python 3 Tutorial from Codeacademy', 'Python for Everybody Specialization','ML with python'],
        'total_durations': 25,
    } ,
    'C':{
        'course_names': ['core c', 'Intermediate c', 'adv c','C Programming For Beginners','C Programming with Linux.'],
        'total_durations': 30,
    } 
}


@app.route('/')
def index():
    return render_template('index.html', courses=courses)

# @app.route('/getcourse/<courseKind>', methods=['GET','POST'])
# def getCourse(courseKind):
#     if courseKind in courses:
#         values=courses[courseKind]

#     return render_template('index.html', values=values)

if __name__ == "__main__":        
    app.run(port=3000, debug=True)
