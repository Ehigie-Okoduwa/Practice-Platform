# Purpose: Set up a FastAPI app with a /health endpoint to confirm the server is running and accessible
# Input: A GET request to /health (no parameters), using FastAPI and Python
# Output: A JSON response with {"status":"OK"}
# Logic: Import FastAPI, create a FastAPI app instance, define a /health endpoint using @app.get, and
#         return a JSON status message with an async function

# Comments for JSON question bank 
# Purpose: Create a test question bank with hard-coded questions for students to use in the app
# Input: 10 hard-coded questions with a mix of multiple-choice and short-answer, covering a few topics
# Output: A JSON file with a list of 10 question objects
# Logic: Create a list of JSON objects, each with id, text, type, options (if multiple-choice), answer, and topic

from fastapi import FastAPI, HTTPException
import json as json

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status":"OK"}


# Purpose: Serve a list of practice questions from questions.json to users via an API endpoint
# Input: A GET request to /questions (no parameters), using FastAPI and Python
# Output: A JSON array of question objects, or an error message if none found
# Logic: Use FastAPI's @app.get to define a /questions endpoint, read questions.json, return its content as JSON, and handle errors if the file is missing or empty

def load_questions():
     try:
        with open("questions.json","r") as file:
            return json.load(file)
     except FileNotFoundError:
         return []
        
@app.get("/questions")
async def get_questions():
    questions = load_questions()
    if questions:
        return questions
    else:
        raise HTTPException(status_code=404, detail="No questions found, please return to home")
