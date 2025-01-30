# FatSecret API Integration with FastAPI & Streamlit

## Overview
This project integrates the **FatSecret Food Search API** using **FastAPI** with OAuth 2.0 authentication. It also includes a **Streamlit-based UI** for testing API queries.

## Features
- FastAPI backend with OAuth 2.0 authentication
- Food search functionality using FatSecret API
- Streamlit UI for easy testing
- Secure API credentials using environment variables
- Error handling for API requests

## Project Structure
```
/fatsecret-api-fastapi
│── main.py           # FastAPI backend
│── app.py            # Streamlit UI for testing
│── .env              # API credentials (not included in repo)
│── requirements.txt  # Python dependencies
│── README.md         # Project documentation
```

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/ishaan-vashist/fatsecret-fastapi.git
cd fatsecret-fastapi
```

### 2. Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file and add your **FatSecret API credentials**:
```
FATSECRET_CLIENT_ID=your_client_id
FATSECRET_CLIENT_SECRET=your_client_secret
```

## Running the Project
### 1. Start the FastAPI Server
```bash
uvicorn main:app --reload
```
API Docs available at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 2. Start the Streamlit UI
```bash
streamlit run app.py
```
Open in browser: [http://localhost:8501/](http://localhost:8501/)

## Using the API
### Search for Food Items
**Endpoint:** `GET /search_food`
**Example Request:**
```bash
http://127.0.0.1:8000/search_food?query=apple
```
**Response:**
```json
{
    "foods": {
        "food": [
            {
                "food_id": "12345",
                "food_name": "Apple",
                "food_type": "Generic",
                "food_url": "https://www.fatsecret.com/calories-nutrition/apple"
            }
        ]
    }
}
```

## Troubleshooting
### "Invalid IP Address Detected"
- Go to [FatSecret Developer Portal](https://platform.fatsecret.com/)
- Whitelist your public IP
- Restart FastAPI and try again

### API Not Returning Results in Streamlit
- Open FastAPI in the browser:
  [http://127.0.0.1:8000/search_food?query=apple](http://127.0.0.1:8000/search_food?query=apple)
- If the response is empty, check **API credentials** in `.env`

## Technologies Used
- **FastAPI** (Python Backend)
- **OAuth 2.0** (FatSecret API Authentication)
- **Streamlit** (UI for API testing)
- **Requests** (Handling API calls)
- **Uvicorn** (FastAPI server)

## Future Improvements
- Add **unit tests** for API responses
- Improve UI/UX in **Streamlit**
- Deploy on **Cloud (AWS/GCP)** for public access

## Author
Developed by **Ishaan Vashist**  
Contact: [Ishaan](mailto:ishaanvashista@gmail.com)  
