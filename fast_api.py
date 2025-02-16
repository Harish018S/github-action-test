from fastapi import FastAPI, Query, HTTPException
import os

app = FastAPI()

def execute_task(task: str) -> str:
    """
    Simulates task execution. In a real-world scenario, this could involve invoking an LLM, 
    running scripts, or performing automated tasks.
    """
    try:
        # Simulating task execution (replace with actual logic)
        if "fail" in task.lower():
            raise ValueError("Task execution failed due to incorrect input.")
        return f"Task '{task}' executed successfully."
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error.")

@app.post("/run")
def run_task(task: str = Query(..., description="Task description")):
    """Executes a task based on plain-English instructions."""
    result = execute_task(task)
    return {"message": result}

@app.get("/read")
def read_file(path: str = Query(..., description="Path to the file")):
    """Returns the content of a file."""
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found.")
    try:
        with open(path, "r") as file:
            content = file.read()
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error while reading file.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
