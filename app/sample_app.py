from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/visit')
def about():
    return render_template("visit.html")


@app.route('/random')
def random():
    return render_template("random.html")


@app.context_processor
def inject_globals():
    return {
        "rand_posl": [
            "На чужой каравай – роток не разевай.",
            "Копейка рубль бережет.",
            "Не буди лихо, пока оно тихо.",
            "Друг познается в беде.",
            "Работа дураков любит.",
            "Жизнь прожить — не поле перейти.",
            "Кому война, а кому мать родна.",
            "В тихом омуте черти водятся.",
            "Дуракам закон не писан.",
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)
