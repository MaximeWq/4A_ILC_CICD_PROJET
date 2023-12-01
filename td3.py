
from flask import Flask, request, jsonify

app = Flask(__name__)

dictionnaire = {}  # Dictionnaire id/modèle

# Endpoint pour afficher la liste complète
@app.route("/afficher_liste", methods=["GET"])
def afficher_liste():
    return jsonify(dictionnaire)

# Endpoint pour ajouter un élément dans la liste
@app.route("/ajouter_element", methods=["POST"])
def ajouter_element():
    data = request.get_json()
    if 'id' in data and 'modele' in data:
        id_element = data['id']
        modele = data['modele']
        dictionnaire[id_element] = modele
        return jsonify({"message": "Élément ajouté avec succès"})
    else:
        return jsonify({"message": "Requête invalide"}, 400)

# Endpoint pour supprimer un élément dans la liste par ID
@app.route("/supprimer_element/<id_element>", methods=["DELETE"])
def supprimer_element(id_element):
    if id_element in dictionnaire:
        del dictionnaire[id_element]
        return jsonify({"message": f"Élément {id_element} supprimé avec succès"})
    else:
        return jsonify({"message": f"Élément {id_element} introuvable"}, 404)

# Endpoint pour modifier un élément via ID (PUT)
@app.route("/modifier_element/<id_element>", methods=["PUT"])
def modifier_element(id_element):
    if id_element in dictionnaire:
        data = request.get_json()
        modele = data.get('modele', dictionnaire[id_element])  # Utilisez la nouvelle valeur si fournie, sinon conservez l'ancienne
        dictionnaire[id_element] = modele
        return jsonify({"message": f"Élément {id_element} modifié avec succès"})
    else:
        return jsonify({"message": f"Élément {id_element} introuvable"}, 404)

if __name__ == "__main__":
    app.run(debug=True)

