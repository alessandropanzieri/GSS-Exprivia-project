from pymongo import MongoClient
import json

# Connessione al database
client = MongoClient("mongodb://localhost:27017")
db = client["GSSDatabase"]
collection = db["employees"]

# Assuming mongodbrdg outputs a file named 'employees_data.json'
with open('employees_data.json', 'r') as file:
    employees_data = json.load(file)

# Inserimento dei dati nella collezione
collection.insert_many(employees_data)

print("Dati di esempio per 50 dipendenti inseriti con successo.")


# Dati di esempio per 2 dipendenti
employees_data = [
    # Dipendente 1
    {
        "person": {
            "generic_information": {
                "first_name": "John",
                "last_name": "Doe",
                "date_of_birth": "1980-01-01",
                "gender": "Male"
            },
            "photography": "base64_encoded_image_data",
            "contacts": {
                "email": "john.doe@example.com",
                "phone": "+123456789",
                "address": "123 Main St, City"
            }
        },
        "worker": {
            "military_rank": "Commander",
            "current_assignment": "Mission Commander in XXX",
            "current_status": "In Service",
            "service_statuses": [
                {
                    "status": "In Service",
                    "date": "2022-01-01"
                },
                {
                    "status": "Resigned",
                    "date": "2022-05-15"
                }
            ]
        },
        "access_rights": {
            "create": False,
            "modify": False,
            "delete": False
        }
    },
    # Dipendente 2
    {
        "person": {
            "generic_information": {
                "first_name": "Jane",
                "last_name": "Smith",
                "date_of_birth": "1985-05-20",
                "gender": "Female"
            },
            "photography": "base64_encoded_image_data",
            "contacts": {
                "email": "jane.smith@example.com",
                "phone": "+987654321",
                "address": "456 Oak St, Town"
            }
        },
        "worker": {
            "military_rank": "Sergeant",
            "current_assignment": "Patrol Duty",
            "current_status": "In Service",
            "service_statuses": [
                {
                    "status": "In Service",
                    "date": "2022-03-10"
                }
            ]
        },
        "access_rights": {
            "create": True,
            "modify": True,
            "delete": False
        }
    }
]

# Inserimento dei dati nella collezione
collection.insert_many(employees_data)

print("Dati di esempio per 2 dipendenti inseriti con successo.")
