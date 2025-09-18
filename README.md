# CodeAPIs

A curated collection of Python API integration examples and best practices, featuring projects built with FastAPI and Django REST Framework.

![alt text](./site-images/codeapi-banner.png)

## ✨ Features
*   **Structured Examples:** Code is organized by framework, with clear, self-contained examples that cover core functionality such as CRUD (Create, Read, Update, Delete) operations.

*   **FastAPI Examples:** Projects demonstrating FastAPI's key features, including:
    *   Asynchronous request handling (`async`/`await`).
    *   Automatic interactive API documentation (Swagger UI).
    *   Input validation and serialization with Pydantic.
    *   Dependency injection.

*   **Django REST Framework Examples:** Projects covering the robust features of DRF, including:
    *   Class-based views and viewsets.
    *   Advanced serialization techniques.
    *   Built-in authentication and permissions.
    *   Powerful ORM and database integration.

*   **Secure Authentication:** Demonstrates secure and recommended methods for handling API authentication (e.g., using environment variables for API keys and tokens).

*   **Dependency Management:** Each project is configured with its own `requirements.txt` file to simplify dependency management and ensure environment reproducibility.

## 📝 Getting started

### Prerequisites
*   Python 3.8+
*   `pip` for installing dependencies

### Installation and Setup
1.  **Clone the repository:**
    ```sh
    git clone https://github.com/imkjangid/CodeAPIs.git
    cd CodeAPIs
    ```
2.  **Navigate to an example and install dependencies:**
    Choose the framework you want to explore. Each framework has its own sub-directory containing a `requirements.txt` file.

    **For FastAPI:**
    ```sh
    cd fastapi_examples/[project_folder]
    pip install -r requirements.txt
    ```

    OR

    ```sh
    pip install fastapi[all]
    ```

    **For Django REST Framework:**
    ```sh
    cd drf_examples/[project_folder]
    pip install -r requirements.txt
    ```

    OR

    ```sh
    pip install django djangorestframework
    ```

3.  **Run the application:**
    Instructions for running each specific example will be detailed within its respective project folder.

### Your code, your choice.

Thank You!