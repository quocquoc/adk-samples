# Kotobuki - Elderly Companionship Agent

This project implements Kotobuki, an AI-powered agent designed to provide companionship and support for elderly users. The agent aims to alleviate loneliness through natural conversation and offers integrated tools for essential communication and information access.

## Overview

Kotobuki leverages Gemini to engage users in meaningful conversation, offer emotional support, and discuss various topics. It also provides easy access to tools for contacting healthcare professionals, caregivers, emergency services, and relatives, as well as searching the internet.

## Agent Details

The key features of the Kotobuki Agent include:

| Feature            | Description                                      |
| ------------------ | ------------------------------------------------ |
| _Interaction Type_ | Conversational, Empathetic                       |
| _Complexity_       | Intermediate                                     |
| _Agent Type_       | Single Agent                                     |
| _Components_       | Tools, Live Conversation (Gemini Live API)       |
| _Vertical_         | Healthcare / Eldercare                           |

### Agent Architecture

*(Optional: Add an architecture diagram specific to Kotobuki if desired)*

The agent uses a conversational AI model (Gemini) enhanced with specific tools to perform actions on behalf of the user. It aims to provide a seamless interface for communication and information retrieval, reducing the complexity often associated with digital tools for elderly users.

*(Note: Tool implementations are currently mocked. Real-world integration would require connecting to actual calling APIs, booking systems, and web search services.)*

### Key Functionalities

- **Conversation & Companionship:**
  - Engages in natural, empathetic conversation.
  - Offers emotional support and discusses various topics.
  - Aims to reduce loneliness and provide companionship.
  - Leverages Gemini Live API for real-time interaction.
- **Integrated Support Tools:**
  - **Make Phone Calls:** Facilitates calls to doctors, nurses, caregivers, emergency services, and relatives.
  - **Book Medical Appointments:** Assists users in scheduling medical appointments.
  - **Search Internet:** Helps users find information online.

#### Tools

The agent has access to the following mocked tools:

- `make_phone_call(contact_type: str, contact_details: str)`: Initiates a phone call to a specified contact.
- `book_medical_appointment(details: str)`: Books a medical appointment.
- `search_internet(query: str)`: Performs an internet search.

## Setup and Installations

### Prerequisites

- Python 3.11+
- Poetry (for dependency management)
- Google ADK SDK (installed via Poetry)
- Google Cloud Project (for Vertex AI Gemini integration, including Gemini Live API access)

### Installation
1.  **Prerequisites:**

    For Agent Engine deployment and Gemini Live API usage, you will need a Google Cloud Project. Once created, [install the Google Cloud SDK](https://cloud.google.com/sdk/docs/install) and authenticate:
    ```bash
    gcloud auth login
    ```
    Enable the necessary APIs:
    ```bash
    gcloud services enable aiplatform.googleapis.com
    ```

2.  Navigate to the Kotobuki agent directory:

    ```bash
    # Assuming you are in the google-adk-samples root directory
    cd agents/kotobuki
    ```

3.  Install dependencies using Poetry:

    If you haven't installed Poetry, run `pip install poetry` first.
    ```bash
    poetry install
    ```
    Activate the virtual environment:
    ```bash
    poetry shell # or poetry env activate
    ```

4.  Set up Google Cloud credentials:

    - Ensure you have a Google Cloud project and the Vertex AI API is enabled.
    - Set the `GOOGLE_GENAI_USE_VERTEXAI`, `GOOGLE_CLOUD_PROJECT`, and `GOOGLE_CLOUD_LOCATION` environment variables (e.g., in a `.env` file created from `.env_sample` or directly in your shell). You might need specific credentials or configurations for Gemini Live API access.

    ```bash
    # Example environment variables
    export GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID_HERE
    export GOOGLE_GENAI_USE_VERTEXAI=1
    export GOOGLE_CLOUD_LOCATION=us-central1
    ```

## Running the Agent

Run the agent using the ADK CLI from the `agents/kotobuki` directory:

1.  Run agent in CLI:
    ```bash
    adk run kotobuki
    ```

2.  Run agent with ADK Web UI:
    ```bash
    # From the google-adk-samples root directory
    adk web
    ```
    Then select `kotobuki` from the dropdown in the Web UI.

### Example Interaction

*(Add a relevant example interaction for Kotobuki here)*

## Evaluating the Agent

*(Adapt evaluation steps and data for Kotobuki)*

**Steps:**

1.  **Run Evaluation Tests:**
    ```bash
    pytest eval
    ```

## Unit Tests

*(Adapt unit tests for Kotobuki tools and logic)*

**Steps:**

1.  **Run Unit Tests:**
    ```bash
    pytest tests/unit
    ```

## Configuration

Configuration parameters like agent name, model, etc., can be found in [kotobuki/config.py](./kotobuki/config.py).

## Deployment on Google Agent Engine

*(Adapt deployment steps for Kotobuki)*

1.  **Build Kotobuki Agent WHL file**
    ```bash
    # Ensure you are in the agents/kotobuki directory
    poetry build --format=wheel --output=deployment
    ```

2.  **Deploy the agent to Agent Engine**
    ```bash
    cd deployment
    python deploy.py # Ensure deploy.py is updated for Kotobuki
    ```

### Testing deployment

*(Adapt testing script for the deployed Kotobuki agent)*

```python
import vertexai
from kotobuki.config import Config # Updated import
from vertexai.preview.reasoning_engines import AdkApp


configs = Config()

vertexai.init(
    project="<YOUR_PROJECT_ID>",
    location="<YOUR_LOCATION>"
)

# Get the deployed agent engine resource name
agent_engine = vertexai.agent_engines.get('projects/PROJECT_ID/locations/LOCATION/reasoningEngines/REASONING_ENGINE_ID')

# Example query
for event in agent_engine.stream_query(
    # user_id=USER_ID, # Define user_id if needed
    # session_id=session["id"], # Define session_id if needed
    message="Hello, I'm feeling a bit lonely today.",
):
    print(event)
```
