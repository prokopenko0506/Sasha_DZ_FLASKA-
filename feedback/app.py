from flask import Flask, render_template, request

app = Flask(__name__)


@app.route(rule="/feedback",methods=["GET", "POST"])
def appointment():
    error = None
    error_2 = None
    error_3 = None
    re = None
    if request.method == "POST":
        name = request.form["name"]
        if len(name) <= 0:
            error = "Введите Имя!"
        email = request.form["email"]
        if "@" not in email:
            error_2 = "Email должен быть с @ !"
        message = request.form["message"]
        if len(message) <= 0:
            error_3 = "Введите своё сообщение!"
        if not error and not error_2 and not error_3:
            re = "Спасибо за запись!"
    return render_template("feedback.html", error=error, error_2=error_2, error_3=error_3,re=re)



if __name__ == "__main__":
    app.run(debug=True)
