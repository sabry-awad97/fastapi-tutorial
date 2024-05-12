# FastAPI Project

This repository contains a FastAPI application designed to manage items through a RESTful API, interfacing with a MongoDB database. The application supports comprehensive CRUD (Create, Read, Update, Delete) operations for item management.

## Key Features

- **Create Items**: Enables the addition of new items to the database.
- **Retrieve Items**: Allows fetching details of either all items or a specific item by ID.
- **Update Items**: Facilitates modifications to the details of existing items.
- **Delete Items**: Permits the removal of items from the database.

## Technologies Employed

- FastAPI: A modern, fast web framework for building APIs with Python.
- Uvicorn: An ASGI (Asynchronous Server Gateway Interface) server for Python.
- Pydantic: Data validation and settings management using Python type annotations.
- MongoDB: A NoSQL database known for its high performance and flexibility.

## Installation

To set up this project locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To launch the server, execute the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will be accessible at `http://0.0.0.0:8000`.

## API Endpoints

- **Base Endpoint**:
  - `GET /`: Returns a welcome message.
- **Item Management**:
  - `POST /items/`: Endpoint to create a new item.
  - `GET /items/`: Endpoint to list all items.
  - `GET /items/{item_id}`: Endpoint to retrieve an item by its ID.
  - `PUT /items/{item_id}`: Endpoint to update an item by its ID.
  - `DELETE /items/{item_id}`: Endpoint to delete an item by its ID.

## Contributing

Contributors are welcome to enhance the functionalities of this project. Please ensure you adhere to the established coding standards and include tests for new features.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
