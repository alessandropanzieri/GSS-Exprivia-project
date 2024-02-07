from pymongo.mongo_client import MongoClient

cluster = MongoClient("mongodb://localhost:27017")
database = cluster.gss_db

all_collections = database.list_collection_names()
for collection in all_collections:
    database.drop_collection(collection)

events_collection = database.events_collection
operators_collection = database.operators_collection
administratives_collection = database.administratives_collection

operators_collection.insert_many([
    {
        "operator_id" : "001",
        "first_name" : "Samuele",
        "last_name" : "Cristiani",
        "birthdate" : "25/03/1990",
        "phone" : "333 445 1819",
        "email" : "scristiani@abc.com",
        "rank" : "soldier",
        "assignment" : "soldier in Lebanon",
        "current_status" : "active"
    },
    {
        "operator_id" : "002",
        "first_name" : "Marina",
        "last_name" : "Saluti",
        "birthdate" : "05/07/1980",
        "phone" : "335 325 5863",
        "email" : "msaluti@abc.com",
        "rank" : "sergeant",
        "assignment" : "sergeant at Taranto regiment",
        "current_status" : "active"
    },
    {
        "operator_id" : "003",
        "first_name" : "Giuseppe",
        "last_name" : "Carotenuto",
        "birthdate" : "09/12/1953",
        "phone" : "331 446 9899",
        "email" : "gcarotenuto@abc.com",
        "rank" : "colonel",
        "assignment" : "colonel at Cecchignola barracks",
        "current_status" : "retired"
    },
    {
        "operator_id" : "004",
        "first_name" : "Franco",
        "last_name" : "Bianchi",
        "birthdate" : "30/09/1972",
        "phone" : "327 669 2253",
        "email" : "fbianchi@abc.com",
        "rank" : "corporal major",
        "assignment" : "corporal major at Benevento regiment",
        "current_status" : "fired"
    },
    {
        "operator_id" : "005",
        "first_name" : "Silvana",
        "last_name" : "Tesori",
        "birthdate" : "22/03/1978",
        "phone" : "329 469 2580",
        "email" : "stesori@abc.com",
        "rank" : "marshal",
        "assignment" : "marshal at Torino regiment",
        "current_status" : "active"
    },
    {
        "operator_id" : "006",
        "first_name" : "Sergio",
        "last_name" : "Ciotti",
        "birthdate" : "21/05/1980",
        "phone" : "323 222 9012",
        "email" : "sciotti@abc.com",
        "rank" : "lieutenant",
        "assignment" : "lieutenant at Naples regiment",
        "current_status" : "active"
    },
    {
        "operator_id" : "007",
        "first_name" : "Clarissa",
        "last_name" : "Vicoli",
        "birthdate" : "17/08/1983",
        "phone" : "366 717 8886",
        "email" : "cvicoli@abc.com",
        "rank" : "captain",
        "assignment" : "captain at Rome regiment",
        "current_status" : "active"
    },
    {
        "operator_id" : "008",
        "first_name" : "Saverio",
        "last_name" : "Lassandro",
        "birthdate" : "17/04/1968",
        "phone" : "324 566 7584",
        "email" : "slassandro@abc.com",
        "rank" : "division general",
        "assignment" : "division general at Bari regiment",
        "current_status" : "active"
    }
])

events_collection.insert_many([
    {
        "event_id" : "01",
        "employee_id" : "008",
        "date" : "12/06/2013",
        "description" : "command post n.1 at US military Airport in South Korea"
    },
    {
        "event_id" : "02",
        "employee_id" : "009",
        "date" : "17/08/2007",
        "description" : "construction supervision at the fortified base on Mount Ortles"
    },
    {
        "event_id" : "03",
        "employee_id" : "008",
        "date" : "10/01/1993",
        "description" : "reinforcement for Canary Islands missile outpost"
    },
    {
        "event_id" : "04",
        "employee_id" : "007",
        "date" : "13/11/2000",
        "description" : "command of the platoon sent to Syria"
    },
    {
        "event_id" : "05",
        "employee_id" : "007",
        "date" : "05/07/1990",
        "description" : ""
    }
])

administratives_collection.insert_many([
    {
        "admin_id" : "010",
        "first_name" : "Giorgio",
        "last_name" : "Manganello",
        "birthdate" : "15/11/1999",
        "phone" : "345 765 8882",
        "email" : "gmanganello@abc.com",
        "current_status" : "active"
    },
    {
        "admin_id" : "011",
        "first_name" : "Elena",
        "last_name" : "Fiorellini",
        "birthdate" : "07/06/2000",
        "phone" : "349 178 3456",
        "email" : "efiorellini@abc.com",
        "current_status" : "active"
    },
    {
        "admin_id" : "012",
        "first_name" : "Fiamma",
        "last_name" : "Ciccioli",
        "birthdate" : "04/08/1994",
        "phone" : "334 883 6162",
        "email" : "fciccioli@abc.com",
        "current_status" : "active"
    }
])