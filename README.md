# tasktrek_api
## Description:
TaskTrek API is a robust solution for user registration and user profile management. The API facilitates the creation, retrieval, updating, and deletion of user accounts and their associated profiles. Upon user creation, a profile is automatically generated, complete with predefined data, streamlining the onboarding process.
#### Key Features
* User Management: Users can be easily created, retrieved, updated, and deleted through dedicated endpoints.
* Automatic Profile Generation: Every user is accompanied by an automatically generated profile, reducing the need for manual setup.
* CRUD Operations on Profiles: Users can perform CRUD (Create, Read, Update, Delete) operations on their profiles and associated data.
 Structured Endpoints: The API provides well-organized endpoints for both user and user profile operations, ensuring clarity and ease of use.
### Available endpoints
#### Users endpoints
#### GET   api/account/users
* lists all users
#### POST   api/account/users
* Create a new user
#### DELETE   api/account/users/1
* delete the user with the id of 1
#### PUT  api/account/users/1
* update the user with the id of 1
#### Usersprofile endpoints
### GET api/account/profile
* list all users profile
#### Getting Started
##### Clone the Repository:
* git clone https://github.com/your-username/tasktrek-api.git
##### Install dependencies
* cd tasktrek-api
  pip install -r Requirnment.txt
##### Configure the Database:
* Update the database connection details in settings.py

##### Run the Application:
* python manage.py runserver
##### Access the Api
* The API can be accessed at http://localhost:8000.

#### API Documentation
For detailed information on the API endpoints, request/response examples, and usage guidelines, refer to the https://web-02.codezenith.com/api/schema/docs/

#### Contributing
If you're interested in contributing to the development of TaskTrek API, please follow the contribution guidelines.

#### License
This project is licensed under the MIT License - see the LICENSE file for details.
.
  


