from flask import Flask, request, jsonify,render_template
import spacy
from  .loadData import docs

app = Flask(__name__)

# load the pretrained language model from spacy
nlp = spacy.load("en_core_web_md")
# this function serves as finding the top k similarities given query and docs(a list of strings)
def find_top_similarities(query, docs, top_k=5):
    query_doc = nlp(query)
    
    similarities = [(doc, query_doc.similarity(doc)) for doc in docs]
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]
    return similarities
# flask as framework
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    """
    The `match` function takes in test audiences, finds the top similarities for each audience
    description, and returns a list of candidates with their similarities.
    :return: The `match` route in the Flask application is returning a JSON response containing the
    output segments with their corresponding segment IDs, descriptions, and a list of candidate matches
    for each test audience segment. The candidates include their IDs, descriptions, and similarity
    scores. See exampleOutput.json as an Instance
    """
    data = request.get_json(force=True)
    test_audiences = data["test_audiences"]
    
    results = []

    for audience in test_audiences:
        segment_id = audience["segment_id"]
        description = audience["description"]
        top_similarities = find_top_similarities(description, docs)
        candidates = [
            {
                "candidate_id": "", #id(doc), # TODO: show the candidates' ID 
                "candidate_descriptionAndName": doc.text,
                "similarity": similarity
            }
            for doc, similarity in top_similarities
        ]
        results.append({
            "segment_id": segment_id,
            "description": description, 
            "candidates": candidates
        })
    
    return jsonify({"output_segment": results})

if __name__ == '__main__':
    app.run(debug=True)
