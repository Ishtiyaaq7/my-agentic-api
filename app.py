from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your custom agentic API!"}

@app.post("/run-agent")
def run_agent(input: dict):
    # This is where you’d put your agent logic
    user_input = input.get("prompt", "No prompt provided.")
    # Example: just echo back
    return {"response": f"Agent received: {user_input}"}
