# TODO Project with DRF and DRF Token Auth

This project is a simple TODO application built using Django Rest Framework (DRF) and DRF Token Authentication. It allows users to register, create, retrieve, update, and delete TODO items through a RESTful API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sarthak7509/DRF-TODO-API.git
   ```
2. Navigate to the project directory:
   ```bash
   cd project-directory
   ```
3. Create a virtual environment (optional, but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the database:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Endpoints

![Alt Text](/samples//enpoints.png)
The following endpoints are available in the API:

### `/api/register`

- **Method:** POST
- **Description:** Register a new user in the system.
- **Request Body:**
  - `username`: The username of the user.
  - `password`: The password of the user.
- **Response:** Returns a JSON response with the user's details.

### `/api/Todo/`

- **Method:** GET
- **Description:** Fetch all the TODO items.
- **Authorization:** Token authentication required. Include the token in the request headers.
- **Response:** Returns a JSON response with all the TODO items.

- **Method:** POST
- **Description:** Create a new TODO item.
- **Authorization:** Token authentication required. Include the token in the request headers.
- **Request Body:**
  - `title`: The title of the TODO item.
  - `description`: The description of the TODO item.
- **Response:** Returns a JSON response with the newly created TODO item.

### `/api/TODO/{id}`

- **Method:** GET
- **Description:** Retrieve a specific TODO item by its ID.
- **Authorization:** Token authentication required. Include the token in the request headers.
- **Response:** Returns a JSON response with the TODO item matching the specified ID.

- **Method:** PUT
- **Description:** Update a specific TODO item by its ID.
- **Authorization:** Token authentication required. Include the token in the request headers.
- **Request Body:**
  - `title`: The updated title of the TODO item.
  - `description`: The updated description of the TODO item.
- **Response:** Returns a JSON response with the updated TODO item.

- **Method:** PATCH
- **Description:** Partially update a specific TODO item by its ID.
- **Authorization:** Token authentication required. Include the token in the request headers.
- **Request Body:** Accepts the same parameters as the PUT method for updating.
- **Response:** Returns a JSON response with the updated TODO item.

- **Method:** DELETE
- **Description:** Delete a specific TODO item by its ID.
- **Authorization:** Token authentication required. Include the token in the request headers.
- **Response:** Returns a JSON response indicating the successful deletion of the TODO item.

### `/api/Token/`

- **Method:** POST
- **Description:** Log in a user and obtain an authentication token.
- **Request Body:**
  - `username`: The username of the user.
  - `password`: The password of the user.
- **Response:** Returns a JSON response with the authentication token.

To create or fetch a TODO item, the user must include the authentication token returned by `/api/Token/` in the request headers under the `Authorization`
