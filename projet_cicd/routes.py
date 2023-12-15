from flask import Flask, request, jsonify
import csv
import sys
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta



app = Flask(__name__)

events = {
    "event1": {"T1": "2023-12-01T12:00:00", "t": 3600, "p": ["person1", "person2"], "n": "Event 1", "d": "Description 1"},
    "event2": {"T1": "2023-11-30T14:00:00", "t": 7200, "p": ["person2", "person3"], "n": "Event 2", "d": "Description 2"},
}

# E1 - Créer un évènement
# curl -X POST -H "Content-Type: application/json" -d "{\"T1\": \"2023-12-03T15:30:00\", \"t\": 1800, \"p\": [\"person3\", \"person4\"], \"n\": \"Event 3\", \"d\": \"Description 3\"}" http://localhost:5000/add-events
@app.route("/add-events", methods=["POST"])
def create_event():
    data = request.get_json()
    event_name = data["n"]
    events[event_name] = data
    return jsonify({"message": "Event created"}), 201

# E2 - Afficher une liste de tous les événements dans l’ordre chronologique
@app.route("/display-events", methods=["GET"])
def get_events():
    sorted_events = sorted(events.values(), key=lambda x: x["T1"])
    return jsonify({"events: ": sorted_events}), 200

# E3 - Afficher une liste de tous les évènements dans l’ordre chronologique liées à une personne
@app.route("/display-events/<person>", methods=["GET"])
def get_events_by_person(person):
    person_events = []
    for event in events.values():
        if person in event["p"]:
            person_events.append(event)
    sorted_person_events = sorted(person_events, key=lambda x: x["T1"])
    return jsonify({"events": sorted_person_events}), 200

# E4 - Ajouter un participant à un évènement
#curl -X POST -H "Content-Type: application/json" -d "{\"participant\": \"nouveau_participant\"}" http://localhost:5000/add-participants/event1/participants
@app.route("/add-participants/<event_name>/participants", methods=["POST"])
def add_participant(event_name):
    data = request.get_json()
    if event_name in events:
        events[event_name]["p"].append(data["participant"])
        return jsonify({"message": "Participant added"}), 200
    return jsonify({"error": "Event not found"}), 404

# E5 - Afficher le détails du prochain cours
@app.route("/display-next-event", methods=["GET"])
def get_next_event():
    if events:
        next_event = min(events.values(), key=lambda x: x["T1"])
        return jsonify({"next_event": next_event}), 200
    else:
        return jsonify({"message": "No events available"}), 404

        
    # E6 - Importer des données depuis un fichier csv
# curl -X POST -F "file=@events.csv" http://localhost:5000/import-csv
@app.route("/import-csv", methods=["POST"])
def import_csv():
    try:                                 # Utilisation du bloc try-except pour gérer les exceptions potentielles lors de l'importation du fichier CSV
        if "file" not in request.files:
            return jsonify({"error": "No file found"}), 400     # On vérifie si le fichier est bien présent dans la requête

        file = request.files["file"]                            # On récupère le fichier
        if file.filename == "":
            return jsonify({"error": "File name is empty"}), 400        #On vérifie que le nom du ficher n'est pas vide

        filename = secure_filename(file.filename)               #Conversion en un format adapté pour Flask
        file.save(filename)                                     #Sauvegarde du fichier
        events.clear()                                          #On vide le dictionnaire d'évènement actuel

        with open(filename, 'rt', encoding='utf-8') as csvfile:     #On ouvre le fichier csv en mode lecture de texte
            csv_data = csv.reader(csvfile, delimiter=',')           #On lit le fichier csv avec le délimiteur ','
            for row in csv_data:
                event_name = row[0]                                 #On récupère le nom de l'évènement
                events[event_name] = {                              #On ajoute les colonnes lues au dictionnaire
                    "T1": row[1],
                    "t": int(row[2]),
                    "p": row[3].split(","),
                    "n": event_name,
                    "d": row[4]  
                }

        return jsonify({"message": "CSV data imported"}), 200
    except Exception as e:
        return jsonify({"error: ": str(e)}), 500
    

# E7 - Obtenir le temps total passé dans des évènements pour une personne
# curl http://localhost:5000/time/person1
@app.route("/time/<person>", methods=["GET"])
def get_time(person):
    time_today = 0
    time_seven_days = 0
    time_month = 0
    current_time = datetime.now()
    seven_days_ago = current_time - timedelta(days=7)
    last_month = datetime(current_time.year, current_time.month - 1, current_time.day) if current_time.month > 1 else datetime(current_time.year - 1, 12, current_time.day)

    for event in events.values():
        if person in event["p"] and len(event["p"]) > 1:
            if datetime.fromisoformat(event["T1"]).date() == current_time.date():
                time_today += event["t"]
            if datetime.fromisoformat(event["T1"]) >= seven_days_ago:
                time_seven_days += event["t"]
            if datetime.fromisoformat(event["T1"]) >= last_month:
                time_month += event["t"]
    return jsonify({
        "Amount of time today": time_today,
        "Amount of time last seven days": time_seven_days,
        "Amount of time last month": time_month
    }), 200

# E8 - Calculer le temps restant avant une date ou un évènement
# curl http://localhost:5000/time-left/2023-12-25
@app.route("/time-left/<date>", methods=["GET"])
def get_time_left(date):
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d")
        current_time = datetime.now()

        if target_date > current_time:
            time_left = target_date - current_time
            return jsonify({"time left": str(time_left)}), 200
        else:
            return jsonify({"message": "The date has already passed"}), 400
    except ValueError:
        return jsonify({"error": "Wrong format. Use: YYYY-MM-DD"}), 400

    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if(sys.argv[1] == "check_syntax"):
            print("Build OK")
            exit(0)
        else:
            print("Passed argument no supported! Support arguments: check_syntax")
            exit(1)
    app.run(debug=True)