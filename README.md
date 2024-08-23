# Kangacook Django Project

## Setup and Run Django Server

## Prerequisites
- Python 3.x
- pip (Python package installer)
- Node.js and npm (for React app)


## React Client

- The backend is configured with CORS to allow calls only from the React app running at `http://localhost:3000`.
- Ensure the Django server is running before starting the React app.

## Steps

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```
   
5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```
   
6 **Run the Django development server:**
    ```sh
    python manage.py runserver
    ```

The Django server will be running at `http://127.0.0.1:8000`.
