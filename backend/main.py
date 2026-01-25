from account.routes import account_router
from actions.routes import action_router
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from tools.automatics import shutdown, startup

app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    title="Dino API Server",
    description="Created and owned by Corgo LC",
    summary="Tech stack: Language(Python), API(FastAPI), UI(Swagger)",
    contact={
        "name": "Hunter Salazar",
        "email": "Hunter.Salazar@bon.nm.gov",
    },
)
app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)


@app.get("/", include_in_schema=False)
async def redirect_to_docs() -> RedirectResponse:
    """Redirect index to the Swagger"""
    return RedirectResponse(url="/docs")


app.include_router(account_router, tags=["Account"], prefix="/account")
app.include_router(action_router, tags=["Movement"], prefix="/actions")
