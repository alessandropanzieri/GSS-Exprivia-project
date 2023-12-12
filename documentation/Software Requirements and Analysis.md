# Software Requirements and Analysis

## Frontend

- **FE - 01**

  The user interface will allow users to navigate employee data, such as:

  *as person*

  - personal information (name, surname, date of birth)
  - photography
  - contacts (mobile number, email)

  *as worker*

  - qualification (the military rank, years of service)
  - any current assignment (e.g. mission commander in xxx)
  - current status (in service/resigned/fired/retired)
  - chronology of service statuses, associated with a date

- **FE - 02**

  The user interface will allow to filter the user research by department, years of service, etc...

- **FE - 03**

  The user interface will allow specific users to modify these employee data.

## Backend

- **BE - 01**

  The system backend will be based on REST-API, ensuring access to employee data.

- **BE - 02**

  The system will expose an authentication mechanism based on JWT tokens to protect user information.

- **BE - 03**

  In order to secure communication between the frontend and backend, communication between frontend and backend will be sured by an SSL channel.

## Database

- **DB - 01**

  In order to store employees' data, a non-relational database will be used.

- **DB - 02**

  Each document contains employee's data.

- **DB - 03**

  Each document has an unique id, in order to search or update each employee's data.
