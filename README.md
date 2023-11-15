# Flask CRUD Application with MongoDB

This is a simple Flask application demonstrating CRUD (Create, Read, Update, Delete) operations with MongoDB. The application allows you to manage information about individuals, such as their name, age, and occupation.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python
- Flask
- pymongo

You can install the required Python packages using the following command:

```bash
pip install Flask pymongo
```

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/Anyel-ec/POO-Mongo-Py/new/main
    ```

2. Navigate to the project directory:

    ```bash
    cd POO-Mongo-Py
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

   The application will run on `http://127.0.0.1:5000/` by default.

## Usage

### 1. View All Persons

- Endpoint: `/`
- Method: GET
- Description: Retrieves and displays information about all persons in the database.

### 2. Create a New Person

- Endpoint: `/`
- Method: POST
- Description: Adds a new person to the database.

    - Parameters:
        - `nombre` (string): The name of the person.
        - `edad` (integer): The age of the person.
        - `ocupacion` (string): The occupation of the person.

### 3. Edit Person Information

- Endpoint: `/editar/<nombre>`
- Method: POST
- Description: Modifies information about an existing person in the database.

    - Parameters:
        - `nombre` (string): The name of the person to be edited.
        - `apellido` (string): The new name for the person.

### 4. Delete a Person

- Endpoint: `/eliminar/<nombre>`
- Method: POST
- Description: Deletes a person from the database.

    - Parameters:
        - `nombre` (string): The name of the person to be deleted.

## MongoDB Configuration

- MongoDB Connection URI: `mongodb://localhost:27017/`
- Database Name: `Prueba`
- Collection Name: `personas`

Make sure MongoDB is running on your local machine or update the connection URI accordingly.

## Notes

- The application uses a `Persona` class to represent an individual and a `ManejadorPersona` class to handle CRUD operations.

- The application runs in debug mode (`app.run(debug=True)`) for development purposes. Ensure to turn off debug mode in a production environment.

Feel free to customize and extend the application based on your requirements.
