# Authentication

This project is a Django-based authentication system that provides both
a traditional Django UI as well as REST API endpoints
(via Django REST Framework) for modern web or mobile applications.

## Features

-   User registration, login, password reset, and logout (via UI and API).
-   JWT (JSON Web Token) authentication for secure stateless API access.
-   Separation of UI (`accounts` app) and API (`accounts_api`
    app).

## Tech Stack

-   **Backend**: Django, Django REST Framework (DRF)
-   **Authentication**: JWT (via `djangorestframework-simplejwt`)
-   **Database**: SQLite (default) but supports
    alternatives in production
-   **Version Control**: Git + GitHub

## Project Structure

    project_root/
    │── accounts/          # Traditional Django authentication app (UI)
    │── accounts_api/      # DRF authentication endpoints
    │── authproject/       # Project settings & URLs
    │── templates/         # HTML templates for UI
    │── .env               # Environment variables (SECRET_KEY, DEBUG, etc.)
    │── .gitignore         # Git ignore file
    │── manage.py
    │── README.md
    │── requirements.txt

## API Endpoints

-   `POST /api/auth/register/` → Register new user
-   `POST /api/auth/login/` → Login user, returns JWT token
-   `POST /api/auth/logout/` → Logout user (invalidate refresh token)
-   `POST /api/auth/token/refresh/` → Get new access token with refresh

## Setup Instructions

1.  Clone the repository:

    ``` bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2.  Create and activate a virtual environment:

    ``` bash
    python -m venv .venv
    source .venv/bin/activate   # Unix-based
    .venv\Scripts\activate    # Windows
    ```

3.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

4.  Create `.env` file in the project root:

    ``` env
    SECRET_KEY=your-django-secret-key
    DEBUG=True
    ```

5.  Run migrations and start server:

    ``` bash
    python manage.py migrate
    python manage.py runserver
    ```

6.  Visit API at:

    -   API Docs/UI: `http://127.0.0.1:8000/api/auth/`
    -   Django UI: `http://127.0.0.1:8000/accounts/`

## Testing

You can interact with the Django Ui as you normally would

For the API, you can test in three ways: - Django REST Framework's built-in
browsable API UI - Postman - curl commands

