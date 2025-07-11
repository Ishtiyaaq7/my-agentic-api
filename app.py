

from fastapi import Form

@app.post("/run-agent", response_class=HTMLResponse)
async def run_agent_web(request: Request, prompt: str = Form(...)):
    # Do your agent logic here
    return templates.TemplateResponse("index.html", {
        "request": request,
        "response": f"You said: {prompt}"
    })

