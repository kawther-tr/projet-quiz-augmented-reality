from flask import Flask, render_template, jsonify

app = Flask(__name__)

questions = [
    {
        "question": "Quelle est la capitale de la Tunisie ?",
        "choices": ["Tunis", "Sfax", "Sousse", "Nabeul"],
        "answer": "Tunis"
    },
    {
        "question": "Combien font 5 × 3 ?",
        "choices": ["15", "10", "20", "8"],
        "answer": "15"
    },

    {
        "question": "Quelle est la capitale de l'Allemagne ?",
        "choices": ["Berlin", "Madrid", "Vienne", "Prague"],
        "answer": "Berlin"
    },
    {
        "question": "Combien font 9 × 6 ?",
        "choices": ["54", "56", "49", "64"],
        "answer": "54"
    },
    {
        "question": "Quel est le plus grand océan ?",
        "choices": ["Atlantique", "Indien", "Pacifique", "Arctique"],
        "answer": "Pacifique"
    },
    {
        "question": "Qui a peint la Joconde ?",
        "choices": ["Van Gogh", "Picasso", "Léonard de Vinci", "Monet"],
        "answer": "Léonard de Vinci"
    },
    {
        "question": "Combien de jours dans une année bissextile ?",
        "choices": ["365", "366", "364", "367"],
        "answer": "366"
    },
    {
        "question": "Quel est le symbole chimique de l’eau ?",
        "choices": ["O2", "CO2", "H2O", "HO"],
        "answer": "H2O"
    },
    {
        "question": "Quel continent est le plus grand ?",
        "choices": ["Afrique", "Europe", "Asie", "Amérique"],
        "answer": "Asie"
    },
    {
        "question": "Combien font 15 + 27 ?",
        "choices": ["42", "40", "43", "41"],
        "answer": "42"
    },
    {
        "question": "Quel est l'animal le plus rapide sur terre ?",
        "choices": ["Lion", "Guépard", "Cheval", "Tigre"],
        "answer": "Guépard"
    },
    {
        "question": "Quelle planète est appelée la planète rouge ?",
        "choices": ["Mars", "Jupiter", "Vénus", "Saturne"],
        "answer": "Mars"
    },
    {
        "question": "Combien de côtés a un hexagone ?",
        "choices": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "Quelle langue est parlée au Brésil ?",
        "choices": ["Espagnol", "Portugais", "Français", "Anglais"],
        "answer": "Portugais"
    },
    {
        "question": "Quel est le plus grand désert du monde ?",
        "choices": ["Sahara", "Gobi", "Antarctique", "Kalahari"],
        "answer": "Antarctique"
    },
    {
        "question": "Combien font 7 × 8 ?",
        "choices": ["54", "56", "58", "60"],
        "answer": "56"
    },
    {
        "question": "Quel est le plus long fleuve du monde ?",
        "choices": ["Nil", "Amazon", "Yangtsé", "Mississippi"],
        "answer": "Amazon"
    },
    {
        "question": "Quel gaz respirons-nous principalement ?",
        "choices": ["Oxygène", "Azote", "CO2", "Hydrogène"],
        "answer": "Oxygène"
    },
    {
        "question": "Combien de continents y a-t-il ?",
        "choices": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Quel instrument a des touches noires et blanches ?",
        "choices": ["Guitare", "Piano", "Violon", "Batterie"],
        "answer": "Piano"
    }

]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/questions")
def get_questions():
    return jsonify(questions)

if __name__ == "__main__":
    app.run(debug=True)