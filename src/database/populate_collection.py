from pymongo.mongo_client import MongoClient

cluster = MongoClient("mongodb://localhost:27017")
#se gss_db non esiste, lo si crea, altrimenti lo cancelli e ricrei
database = cluster.gss_db
all_collections=database.list_collection_names()
print(all_collections)
for collection in all_collections:
    print(collection)
    database.drop_collection(collection)

operators_collection = database.operators_collection
print(operators_collection)
administrative_collection = database.administrative_collection
event_collection = database.event_collection


#per la collection del personale militare
operators_collection.insert_many([
    {
        "operator_id" :"001",
        "first": "Samuele",
        "last":"Cristiani",
        "birthdate":"25/03/1990",
        "phone":"333 445 1819",
        "email":"scristiani@abc.com",
        "rank":"soldier",
        "assignment":"soldier in Lebanon", 
        "current_status":"active"
    },
    {
        "operator_id" :"002",
        "first": "Marina",
        "last":"Saluti",
        "birthdate":"05/07/1980",
        "phone":"335 325 5863",
        "email":"msaluti@abc.com",
        "rank":"sergeant",
        "assignment":"sergeant at Taranto regiment", 
        "current_status":"active"
    },
    {
        "operator_id" :"003",
        "first": "Giuseppe",
        "last":"Carotenuto",
        "birthdate":"09/12/1953",
        "phone":"331 446 9899",
        "email":"gcarotenuto@abc.com",
        "rank":"colonel",
        "assignment":"colonel at Cecchignola barracks", 
        "current_status":"retired"
    },
    {
        "operator_id" :"004",
        "first": "Franco",
        "last":"Bianchi",
        "birthdate":"30/09/1972",
        "phone":"327 669 2253",
        "email":"fbianchi@abc.com",
        "rank":"corporal major",
        "assignment":"corporal major at Benevento regiment", 
        "current_status":"fired"
    
    
       },
       {
        "operator_id" :"005",
        "first": "Silvana",
        "last":"Tesori",
        "birthdate":"22/03/1978",
        "phone":"329 469 2580",
        "email":"stesori@abc.com",
        "rank":"marshal",
        "assignment":"marshal at Torino regiment", 
        "current_status":"active"
     },
    {
        "operator_id" :"006",
        "first": "Sergio",
        "last":"Ciotti",
        "birthdate":"21/05/1980",
        "phone":"323 222 9012",
        "email":"sciotti@abc.com",
        "rank":"lieutenant",
        "assignment":"lieutenant at Naples regiment", 
        "current_status":"active"
    
    
       },
        {
        "operator_id" :"007",
        "first": "Clarissa",
        "last":"Vicoli",
        "birthdate":"17/08/1983",
        "phone":"366 717 8886",
        "email":"cvicoli@abc.com",
        "rank":"captain",
        "assignment":"captain at Rome regiment", 
        "current_status":"active"
    },
    {
        "operator_id" :"008",
        "first": "Saverio",
        "last":"Lassandro",
        "birthdate":"17/04/1968",
        "phone":"324 566 7584",
        "email":"slassandro@abc.com",
        "rank":"division general",
        "assignment":"division general at Bari regiment", 
        "current_status":"active"
    }
])

# per la collection degli amministrativi

administrative_collection.insert_many([
    {
        "admin_id" :"010",
        "first": "Giorgio",
        "last":"Manganello",
        "birthdate":"15/11/1999",
        "phone":"345 765 8882",
        "email":"gmanganello@abc.com",
        "current_status":"active"
    },
    {
        "admin_id" :"011",
        "first": "Elena",
        "last":"Fiorellini",
        "birthdate":"07/06/2000",
        "phone":"349 178 3456",
        "email":"efiorellini@abc.com",
        "current_status":"active"
    },
    {
        "admin_id" :"012",
        "first": "Fiamma",
        "last":"Ciccioli",
        "birthdate":"04/08/1994",
        "phone":"334 883 6162",
        "email":"fciccioli@abc.com",
        "current_status":"active"
    }
])

# per la collection degli eventi che compongono lo stato di servizio
# degli operatori

event_collection.insert_many([
    {
       "event_id":"01",
        "operator_id":"008",
        "date":"12/06/2013",
        "description":"command post n.1 at US military Airport in South Korea"
       },
    {
       "event_id":"02",
        "operator_id":"009",
        "date":"17/08/2007",
        "description":"construction supervision at the fortified base on Mount Ortles"
       },
    {
       "event_id":"03",
        "operator_id":"008",
        "date":"10/01/1993",
        "description":"reinforcement for Canary Islands missile outpost"
       },
    {
       "event_id":"04",
        "operator_id":"007",
        "date":"13/11/2000",
        "description":"command of the platoon sent to Syria"
       },
    {
       "event_id":"05",
        "operator_id":"007",
        "date":"05/07/1990",
        "description":""
       }
])

collection.update_one(
    {"rango militare": "recluta"},
    {"$set" : {"rango militare": "soldato"}}
)

collection.count_documents({"key": {"$gt": 1}})
collection.delete_one({"key": 1})
collection.delete_many({"key": {"$gt": 1}})


for document in collection.find({"stato attuale":"in servizio"}):
    print(document)

for document in collection.find({"stato attuale":"licenziato"}):
    print(document)

for document in collection.find({"stato attuale":"in servizio"}):
    print(document)

for document in collection.find({"rango militare":"caporal maggiore"}):
    print(document)

for document in collection.find({"rango militare":"soldato"}):
    print(document)

for document in collection.find({"rango militare":"colonnello"}):
    print(document) 

for document in collection.find({"rango militare":"luogotenente"}):
    print(document)

for document in collection.find({"rango militare":"maresciallo"}):
    print(document)

for document in collection.find({"rango militare":"capitano"}):
    print(document)

for document in collection.find({"rango militare":"generale di divisione"}):
    print(document)

for document in collection.find({"rango militare":"generale"}):
    print(document)

for document in collection.find({"data di nascita":"25/03/1990"}):
    print(document)

for document in collection.find({"incarico attuale":"operatore"}):
    print(document)

for document in collection.find({"data":"12/06/2013"}):
    print(document)

for document in collection.find({"id dipendente":"007"}):
    print(document)