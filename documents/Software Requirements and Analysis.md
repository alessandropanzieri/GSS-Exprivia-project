# Software Requirements and Analysis

## Frontend

- **FE - 01**

  The user interface will allow users to navigate employee data, such as:

  *as person*

  - personal information
  - photography
  - contacts

  *as worker*

  - qualification (the military rank)
  - any current assignment (e.g. mission commander in xxx)
  - current status (in service/resigned/fired/retired)
  - chronology of service statuses, associated with a date

- **FE - 02**

  The user interface will allow to filter the user research by department, years of service, etc...

- **FE - 03**

  The user interface will allow specific users to modify these employee data.

## Backend

- **BE - 01**

  The system will be implemented using REST-API backend technology, ensuring access to employee information.

- **BE - 02**

  The system wil be implement an authentication system using Flask-Security and JWT tokens to protect user credentials.

- **BE - 03**

  In order to secure communication between the frontend and backend through, the system will be use JSON Web Tokens too.

## Database

- **DB - 01**

  In order to storage employees' data, non-relational database will be the data-model used.

- **DB - 02**

  Use of a specific employees' collection is provided in order to organize each employee's document.

- **DB - 03**

  Each document contains employee's "as person/worker" information.

- **DB - 04**

  Each document has an unique id, in order to search or update each employee.
