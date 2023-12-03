from flask import Flask, request, jsonify
import csv
import sys

app = Flask(__name__)

events = {
    'event1': {'T1': '2023-12-01T12:00:00', 't': 3600, 'p': ['person1', 'person2'], 'n': 'Event 1'},
    'event2': {'T1': '2023-11-30T14:00:00', 't': 7200, 'p': ['person2', 'person3'], 'n': 'Event 2'},
}

# E1 - Créer un évènement
#curl -X POST -H "Content-Type: application/json" -d '{"T1": "2023-12-03T15:30:00", "t": 1800, "p": ["person3", "person4"], "n": "Event 3"}' http://localhost:5000/add-events
@app.route('/add-events', methods=['POST'])
def create_event():
    data = request.get_json()
    event_name = data['n']
    events[event_name] = data
    return jsonify({'message': 'Event created successfully'}), 201

# E2 - Afficher une liste de tous les événements dans l’ordre chronologique
@app.route('/display-events', methods=['GET'])
def get_events():
    sorted_events = sorted(events.values(), key=lambda x: x['T1'])
    return jsonify({'events': sorted_events}), 200

# E3 - Afficher une liste de tous les évènements dans l’ordre chronologique liées à une personne
@app.route('/display-events/<person>', methods=['GET'])
def get_events_by_person(person):
    person_events = [event for event in events.values() if person in event['p']]
    sorted_person_events = sorted(person_events, key=lambda x: x['T1'])
    return jsonify({'events': sorted_person_events}), 200

# E4 - Ajouter un participant à un évènement
#curl -X POST -H "Content-Type: application/json" -d '{"participant": "nouveau_participant"}' http://localhost:5000/add-participants/event1/participants
@app.route('/add-participants/<event_name>/participants', methods=['POST'])
def add_participant(event_name):
    data = request.get_json()
    if event_name in events:
        events[event_name]['p'].append(data['participant'])
        return jsonify({'message': 'Participant added successfully'}), 200
    return jsonify({'error': 'Event not found'}), 404

# E5 - Afficher le détails du prochain cours
@app.route('/display-next-event', methods=['GET'])
def get_next_event():
    if events:
        next_event = min(events.values(), key=lambda x: x['T1'])
        return jsonify({'next_event': next_event}), 200
    return jsonify({'message': 'No events available'}), 404

# E6 - Importer des données depuis un fichier csv
#curl -X POST -F "file=@events.csv" http://localhost:5000/import-csv
@app.route('/import-csv', methods=['POST'])
def import_csv():
    try:
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        if file:
            # Supprimez les événements existants avant d'importer depuis le fichier CSV
            events.clear()

            # Lecture du fichier CSV
            csv_data = csv.DictReader(file)
            for row in csv_data:
                event_name = row.get('n')
                events[event_name] = {
                    'T1': row.get('T1'),
                    't': int(row.get('t')),
                    'p': row.get('p').split(','),
                    'n': event_name
                }

            return jsonify({'message': 'CSV data imported successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if(sys.argv[1] == "check_syntax"):
            print("Build OK")
            exit(0)
        else:
            print("Passed argument no supported! Support arguments: check_syntax")
            exit(1)
    app.run(debug=True)