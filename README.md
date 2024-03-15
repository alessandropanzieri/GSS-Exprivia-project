# Architectural Document

This project is done by Expriva Spa interns:

- Alejandro Acosta
- Alessandro Panzieri
- Lorenzo Palombi
- Matteo Carbone

We work together with Francesco Fornari, an offering and solutions architect in Exprivia.

Francesco assisted us in simulating a real work project, which consisted of an employees management system for a fake company called Gamma Security Services.

## What is Gamma Security Services?

GSS is a worldwide military private security company (PMSC). For each *on* or *off* duty employee, registered in the management system, it is possible to view a personal card that presents all the following data:

### as person

- generic information
- photography
- contacts

### as GSS employee

- Military rank
- current assignment (e.g. mission commander in xxx)
- current status (in service/resigned/fired/retired)
- chronology of service statuses, associated with a date

Only some users of the system have the possibility to create, modify or delete employee's data, while all others only have the possibility to consult them.

The system is usable via common web browsers, therefore end users haven't to install any software on their workstations. To ensure its maintainability, the system has been developed using cutting-edge technologies and the architecture has an approach open to new features.

## Software Requirements and Analysis

### Frontend

- #### **FE - 01**

  The user interface allows users to navigate employee's data.

- #### **FE - 02**

  The user interface allows to filter the user research by department, years of service, etc...

- #### **FE - 03**

  The user interface allows specific users to modify these employee's data.

### Backend

- #### **BE - 01**

  The system backend is based on REST-API, ensuring access to employee's data.

- #### **BE - 02**

  The system exposes an authentication mechanism based on JWT tokens to protect user information.

- #### **BE - 03**

  Communication between frontend and backend is secured by an SSL channel.

### Database

- #### **DB - 01**

  To store employees' data, a non-relational database is used, such as MongoDB.

- #### **DB - 02**

  Each document contains employee's data.

- #### **DB - 03**

  Each document has a unique id, to search or update each employee's data.

  ![ER model diagram](documentation/ER_model_diagram/ER_model.png)

  This is the ER (entity-relation) model diagram. It represents the schema of the collections used in our DB, including the document. Every operational employee has at least one event assigned. Every event is assigned to one and only operational employee. Since administrators don't have any events assigned to their careers, the administrator employee's collection is free from links to other collections. Here we show some examples of collections stored in the DB:

  - #### **Empoyees collection**

    *"id"* : "007",\
    *"first_name"* : "Clarissa",\
    *"last_name"* : "Vicoli",\
    *"birthdate"* : "17/08/1983",\
    *"email"* : "<cvicoli@abc.com>",\
    *"phone"* : "366 717 8886",\
    *"current_status"* : "active"\
    *"rank"* : "captain",\
    *"assignment"* : "captain at Rome regiment"

  - #### **Administrators collection**

    *"id"* : "010",\
    *"first_name"* : "Giorgio",\
    *"last_name"* : "Manganello",\
    *"birthdate"* : "15/11/1999",\
    *"email"* : "<gmanganello@abc.com>",\
    *"phone"* : "345 765 8882",\
    *"current_status"* : "active"

  - #### **Events collection**

    *"id"* : "01",\
    *"date"* : "12/06/2013",\
    *"description"* : "command post n.1 at US military Airport in South Korea"\
    *"employee_id"* : "008"

## Architecture Diagram

This diagram wants to show the customer how our web app works.

![architecture diagram](documentation/architecture_diagram/architecture.png)

Starting from the first interaction using the UI provided by the frontend, a request process is launched; once a request, the backend asks the model the operations to be performed on the database, which will return an operation result containing the data that will be then shown by the frontend directly to the user.

## Deployment

intro: Tramite la creazione di più macchine virtuali e l'impostazione di una connessione SSH, si vogliono simulare accessi da remoto alla macchina server che mette a disposizione il nostro servizio. Sulle macchine virtuali si è poi deciso di gestire i servizi frontend, backend e database containerizzandoli sfruttando Docker.


Download e installazione della Macchina Virtuale:
Come software per ospitare la Macchina Virtuale è stato scelto VirtualBox di Oracle. Si è voluto simulare un ambiente Linux con sistema operativo Debian (12.5, 64-bit).
E' stata installata con memoria di base 2048 MB, quattro processori, 20 GB di archiviazione. La rete è stata impostata su Scheda con bridge.


Configurazione e starting della VM: Una volta effettuato il primo accesso alla Machhina Virtuale, la si deve configurare. E' stata installata Debian GNU/Linux nella stessa.
Vengono dunque impostati fuso orario, lingua, location, tastiera e Host Name. Viene impostata la password per l'utente root e creato un utente non root. 
Viene infine configurato SSHD per permettere agli utenti di collegarsi tramite connessione SSH.

Connessione SSH e accesso remoto con PuTTY:

E' stata  configurata una connessione SSH (Secure Shell Host) tramite il programma PuTTY con cui è possibile effettuare dal proprio pc un accesso remoto, tramite terminale, alla Macchina Virtuale. Per accedervi sono necessari l'Host Name o l'indirizzo IP della macchina-server e il numero della porta hardware associata alle connessioni SSH (di default 22). Effettuato il login come root si prosegue con la configurazione vera e propria, installando Git, Vim e Docker.

Installazione e utilizzo di Docker:

Installando Docker sono stati suddivisi in container il componente frontend, quello di backend e il database.
La containerizzazione di un'applicazione garantisce che ogni sua componente venga isolata dalle altre in virtuali container. Grazie a questo approccio è possibile dotare il sistema di una maggiore flessibilità.
I container permettono di installare la nostra applicazione in piccoli ambienti isolati e controllati senza doverci curare dell'installazione del sistema operativo.
E' possibile inoltre aggiungere o rimuovere istanze di container, per questioni di scalabilità, senza dover modificare le infrastrutture sottostanti; si può, ancora, riprodurre stessi ambienti di esecuzione su più ambienti, semplificando sviluppo, test e operazione del servizio.


