from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import random
import spacy


nlp = spacy.load('en_core_web_sm')

server = Flask(__name__)
CORS(server)

def preprocess_question(question):
    doc = nlp(question.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return tokens


def get_odu_advice(question, selected_key=None):
    processed_question = preprocess_question(question)

    conn = sqlite3.connect('ifa_divination.db')
    cursor = conn.cursor()
    cursor.execute('SELECT odu_name, verses, advice, keys FROM odu_ifa')
    odus = cursor.fetchall()
    conn.close()

    best_match = None
    best_match_count = 0
    all_keywords = set()

    for odu, verses, advice, keys in odus:
        key_tokens = set(keys.split())
        common_tokens = key_tokens.intersection(processed_question)
        score = len(common_tokens)
        if score > best_match_count:
            best_match_count = score
            best_match = (odu, verses, advice)
        all_keywords.update(key_tokens)

    if best_match and best_match_count > 0:
        return {"odu": best_match[0], "verses": best_match[1],"advice": best_match[2], "keywords": None}
    elif selected_key:
        for odu, advice, keys in odus:
            if selected_key in keys.split():
                return {"odu": odu, "verses": verses,"advice": advice, "keywords": None}
    elif all_keywords:
        random_keywords = random.sample(all_keywords, min(5, len(all_keywords)))
        return {"odu": None, "advice": None, "keywords": random_keywords}
    else:
        return {"odu": None, "advice": "No guidance available at this moment.", "keywords": []}

@server.route('/divine', methods=['POST'])
def divine():
    data = request.get_json()
    question = data.get('question')
    selected_key = data.get('selected_key')
    if not question:
        return jsonify({"error": "Question is required"}), 400

    result = get_odu_advice(question, selected_key)
    if result["odu"]:
        return jsonify({"odu": result["odu"], "verses": result["verses"], "advice": result["advice"]})
    elif not result["keywords"]:
        return jsonify({"odu": None, "advice": "Consult an Ifa Priest for more guidance as I can't help you today!"})
    else:
        return jsonify({"keywords": result["keywords"]})


if __name__ == '__main__':
    server.run(debug=True)
