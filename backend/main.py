# Comments for JSON question bank 
# Purpose: Create a test question bank with hard-coded questions for students to use in the app
# Input: 50 hard-coded questions with a mix of multiple-choice (70%) and short-answer (30%), covering 5 topics
# Output: A JSON file with a list of 50 question objects
# Logic: Create a list of JSON objects, each with id, text, type, options (if multiple-choice), answer, topic, and explanation

from fastapi import FastAPI, HTTPException 
import json

app = FastAPI()

# Purpose: Serve a list of practice questions from questions.json to users via an API endpoint
# Input: A GET request to /questions with an optional 'topic' query parameter (e.g., /questions?topic=algebra), using FastAPI and Python
# Output: A JSON array of question objects matching the topic, or all questions if no topic is specified, or an error message if none found
# Logic: Use FastAPI's @app.get to define a /questions endpoint, read questions.json, filter by topic if provided, return the content as JSON, and handle errors if the file is missing or empty

def load_questions():
    try:
        with open("questions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
@app.get("/questions")
async def get_questions(topic: str = None):
    questions = load_questions()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found, please return to home")
    if topic:
        questions = [q for q in questions if q["topic"] == topic]
    return questions