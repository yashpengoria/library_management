# Library Management System API

This is the backend layer of a Library Management System implemented using FastAPI, MongoDB, and Pydantic.

## Tech Stack

- Language: Python
- Framework: FastAPI
- Database: MongoDB

## Getting Started

To run this application locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/yashpengoria/library_management.git
cd library_management
```

2. Set Up a Virtual Environment (Optional, but recommended)

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Environment Configuration

   - Create a `.env` file and store your `<username>` and `<password>` with your MongoDB Atlas credentials.

5. Run the FastAPI application:

```bash
uvicorn main:app --reload
```

The application should now be running locally at `[http://127.0.0.1:8000]`.

## API Endpoints

### Create Student

- **URL:** `/students`
- **Method:** POST
- **Description:** API to create a student in the system.
- **Request Body:**
  ```json
  {
      "name": "John Doe",
      "age": 25,
      "address": {
          "city": "New York",
          "country": "USA"
      }
  }
  ```
- **Response:**
  ```json
  {
      "id": "6117fc1317deaf103dbd0f68",
      "name": "John Doe",
      "age": 25,
      "address": {
          "city": "New York",
          "country": "USA"
      }
  }
  ```
### Get All Students
- **URL:** `/students`
- **Method:** GET
- **Description:** API to get a list of all students.
- **Response:**
  ```json
  {
      "id": "6117fc1317deaf103dbd0f68",
      "name": "John Doe",
      "age": 25,
      "address": {
          "city": "New York",
          "country": "USA"
      }
  },
  {
      "id": "6117fc1317deaf103dbd0f69",
      "name": "Jane Smith",
      "age": 30,
      "address": {
          "city": "Los Angeles",
          "country": "USA"
      }
  }
  ```


### Update Student

- **URL:** `/students/{id}`
- **Method:** PATCH
- **Description:** API to update a student's information.
- **Request Body:** Provide fields to update (e.g., "name", "age", "address.city", "address.country").
- **Response:**
  ```json
  {
      "message": "Student updated successfully"
  }
  ```

### Fetch Student

- **URL:** `/students/{id}`
- **Method:** GET
- **Description:** API to fetch a student's information by ID.
- **Response:**
  ```json
  {
      "name": "John Doe",
      "age": 25,
      "address": {
          "city": "New York",
          "country": "USA"
      }
  }
  ```

### Delete Student

- **URL:** `/students/{id}`
- **Method:** DELETE
- **Description:** API to delete a student by ID.
- **Response:**
  ```json
  {
      "message": "Student deleted successfully"
  }
  ```
## Screenshots

Swagger UI API Documentation

![image](https://github.com/yashpengoria/library_management/assets/97501212/793b5708-9bad-4618-8d65-0c53c6c7af48)

Get All Studnets

![image](https://github.com/yashpengoria/library_management/assets/97501212/a05d83c6-3032-41e7-b803-eda004bbbb89)

Create Student

![image](https://github.com/yashpengoria/library_management/assets/97501212/2b5ff03a-6fe9-495e-8854-2996e2130480)

Get Student by Id

![image](https://github.com/yashpengoria/library_management/assets/97501212/82760c56-9247-4a40-a10e-13146c56c76b)

Update Student By Id

![image](https://github.com/yashpengoria/library_management/assets/97501212/1a427308-62d9-4c24-b4f3-162521b60ae7)

Delete Student By Id

![image](https://github.com/yashpengoria/library_management/assets/97501212/78fdba0d-900a-4f80-b968-10bbf346adb4)

