# Vertex Chat Permission

This project is a chatbot application built using Streamlit and Vertex AI. It includes user authentication, chat functionality, and integration with a PostgreSQL database for user management.

## Features

- **User Authentication**: Sign-in and sign-up functionality with password hashing.
- **Chatbot**: A conversational AI assistant powered by Vertex AI.
- **Database Integration**: PostgreSQL for storing user data.
- **Custom Tools**: Extendable tools for processing user-specific requests.

## Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose
- Google Cloud credentials for Vertex AI
- PostgreSQL database
- **uv**: Install using `pip install uv`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd vertex-chat-permission
```

### 2. Set Up Environment Variables

Create a `.env` file in the `app` directory with the following variables:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres_db
DB_USER=postgres
DB_PASSWORD=password
GOOGLE_CLOUD_PROJECT_ID=<your-google-cloud-project-id>
GOOGLE_CLOUD_REGION=us-central1
GOOGLE_SERVICE_ACCOUNT_CREDENTIAL_PATH=./credentials/gcp.json
```

Or `cp .env.example .env` and change variables

### 3. Start the Database

Use Docker Compose to start the PostgreSQL database:

```bash
docker-compose up -d
```

### 4. Install Dependencies

Create a virtual environment and install the required Python packages:

```bash
uv sync
```

### 5. Run the Application

Start the Streamlit application:

```bash
uv run streamlit run app/main.py
```

### 6. Access the Application

Open your browser and navigate to `http://localhost:8501`.

## Project Structure

```
vertex-chatbot/
├── app/
│   ├── auth.py                # Authentication logic
│   ├── chat_utils.py          # Chatbot utilities
│   ├── config.py              # Configuration constants
│   ├── db/
│   │   ├── base.py            # Database setup
│   │   ├── config.py          # Database configuration
│   │   ├── models.py          # Database models
│   │   ├── user_repository.py # User repository functions
│   ├── main.py                # Main application entry point
│   ├── vertexai_utils.py      # Vertex AI integration
├── docker-compose.yml         # Docker Compose configuration
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Tools and Libraries

- **Streamlit**: Frontend for the chatbot application.
- **Vertex AI**: Generative AI for chatbot responses.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Database for user management.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai)
- [PostgreSQL](https://www.postgresql.org/)
