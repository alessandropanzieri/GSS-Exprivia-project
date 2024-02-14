from pymongo.mongo_client import MongoClient

cluster = MongoClient("mongodb+srv://username:dalEpB6lf0fPCucs@cluster.f653jhv.mongodb.net/?retryWrites=true&w=majority")
database = cluster.gss_db

collections = database.list_collection_names()
for collection in collections:
    database.drop_collection(collection)

events_collection = database.events_collection
employees_collection = database.employees_collection
administratives_collection = database.administratives_collection

events_collection.insert_many([
    {
        "id" : 1,
        "date" : "12/06/2013",
        "description" : "command post n.1 at US military Airport in South Korea",
        "employee_id" : 1
    },
    {
        "id" : 2,
        "date" : "17/08/2007",
        "description" : "construction supervision at the fortified base on Mount Ortles",
        "employee_id" : 2

    },
    {
        "id" : 3,
        "date" : "10/01/1993",
        "description" : "reinforcement for Canary Islands missile outpost",
        "employee_id" : 3
    },
    {
        "id" : 4,
        "date" : "13/11/2000",
        "description" : "command of the platoon sent to Syria",
        "employee_id" : 4
    },
    {
        "id" : 5,
        "date" : "05/07/1990",
        "description" : "",
        "employee_id" : 5
    }
])

employees_collection.insert_many([
    {
        "id" : 1,
        "first_name" : "Samuele",
        "last_name" : "Cristiani",
        "birthdate" : "25/03/1990",
        "email" : "scristiani@abc.com",
        "phone" : "333 445 1819",
        "current_status" : "active",
        "rank" : "soldier",
        "assignment" : "soldier in Lebanon"
    },
    {
        "id" : 2,
        "first_name" : "Marina",
        "last_name" : "Saluti",
        "birthdate" : "05/07/1980",
        "email" : "msaluti@abc.com",
        "phone" : "335 325 5863",
        "current_status" : "active",
        "rank" : "sergeant",
        "assignment" : "sergeant at Taranto regiment"
    },
    {
        "id" : 3,
        "first_name" : "Giuseppe",
        "last_name" : "Carotenuto",
        "birthdate" : "09/12/1953",
        "email" : "gcarotenuto@abc.com",
        "phone" : "331 446 9899",
        "current_status" : "retired",
        "rank" : "colonel",
        "assignment" : "colonel at Cecchignola barracks"
    },
    {
        "id" : 4,
        "first_name" : "Franco",
        "last_name" : "Bianchi",
        "birthdate" : "30/09/1972",
        "email" : "fbianchi@abc.com",
        "phone" : "327 669 2253",
        "current_status" : "fired",
        "rank" : "corporal major",
        "assignment" : "corporal major at Benevento regiment"
    },
    {
        "id" : 5,
        "first_name" : "Silvana",
        "last_name" : "Tesori",
        "birthdate" : "22/03/1978",
        "email" : "stesori@abc.com",
        "phone" : "329 469 2580",
        "current_status" : "active",
        "rank" : "marshal",
        "assignment" : "marshal at Torino regiment"
    },
    {
        "id" : 6,
        "first_name" : "Sergio",
        "last_name" : "Ciotti",
        "birthdate" : "21/05/1980",
        "email" : "sciotti@abc.com",
        "phone" : "323 222 9012",
        "current_status" : "active",
        "rank" : "lieutenant",
        "assignment" : "lieutenant at Naples regiment"
    },
    {
        "id" : 7,
        "first_name" : "Clarissa",
        "last_name" : "Vicoli",
        "birthdate" : "17/08/1983",
        "email" : "cvicoli@abc.com",
        "phone" : "366 717 8886",
        "current_status" : "active",
        "rank" : "captain",
        "assignment" : "captain at Rome regiment"
    },
    {
        "id" : 8,
        "first_name" : "Saverio",
        "last_name" : "Lassandro",
        "birthdate" : "17/04/1968",
        "email" : "slassandro@abc.com",
        "phone" : "324 566 7584",
        "current_status" : "active",
        "rank" : "division general",
        "assignment" : "division general at Bari regiment"
    }
])

administratives_collection.insert_many([
    {
        "id" : 1,
        "first_name" : "Giorgio",
        "last_name" : "Manganello",
        "birthdate" : "15/11/1999",
        "email" : "gmanganello@abc.com",
        "phone" : "345 765 8882",
        "current_status" : "active"
    },
    {
        "id" : 2,
        "first_name" : "Elena",
        "last_name" : "Fiorellini",
        "birthdate" : "07/06/2000",
        "email" : "efiorellini@abc.com",
        "phone" : "349 178 3456",
        "current_status" : "active"
    },
    {
        "id" : 3,
        "first_name" : "Fiamma",
        "last_name" : "Ciccioli",
        "birthdate" : "04/08/1994",
        "email" : "fciccioli@abc.com",
        "phone" : "334 883 6162",
        "current_status" : "active"
    }
])