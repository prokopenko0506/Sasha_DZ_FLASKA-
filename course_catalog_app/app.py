from flask import Flask, render_template

app = Flask(__name__)



courses = [
    {"title": "Python для начинающих", "level": "beginner", "price": 0},
    {"title": "Flask основы", "level": "middle", "price": 50},
    {"title": "HTML и CSS", "level": "beginner", "price": 30},
    {"title": "SQL база", "level": "middle", "price": 40}
]


@app.route("/")
def home():
    return render_template("home.html",courses_count=len(courses))


@app.route("/courses")
def courses_page():
    free_courses_count = sum(1 for course in courses if course["price"] == 0)

    return render_template("courses.html", courses=courses, free_courses_count=free_courses_count)


if __name__ == "__main__":
    app.run(debug=True)
