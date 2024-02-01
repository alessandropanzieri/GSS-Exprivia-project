# Architectural Document

This project is done by Expriva Spa interns:

- Alejandro Acosta
- Alessandro Panzieri
- Lorenzo Palombi
- Matteo Carbone

We work together with Francesco Fornari, an offering and solutions architect in Exprivia.

Francesco assisted us in simulating a real work project, which consisted of an employee management system for a fake company called Gamma Security Services.

## What is Gamma Security Services?

GSS is a worldwide military private security company (PMSC). For each *on* or *off* duty employee of its, registered in the management system, it is possible to view a personal card that presents all the following data:

### as person

- generic information
- photography
- contacts

### as GSS worker

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

  To store employees' data, a non-relational database is used.

- #### **DB - 02**

  Each document contains employee's data.

- #### **DB - 03**

  Each document has a unique id, to search or update each employee's data.

## Deployment
