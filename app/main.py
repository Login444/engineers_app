from fastapi import FastAPI, HTTPException
from app.entity.team import Team
from app.usecase.team_usecase import TeamUseCase
from app.repository.team_repo import TeamRepository

app = FastAPI()

# Инициализация репозитория и сервисов
team_repository = TeamRepository()
team_usecase = TeamUseCase(repo=team_repository)


@app.post("/teams/", response_model=Team)
async def create_team(team: Team):
    team_usecase.create_team(team)
    return team


@app.put("/teams/{team_id}", response_model=Team)
async def update_team(team_id: str, team: Team):
    if team.id != team_id:
        raise HTTPException(status_code=400, detail="ID in path and body do not match")
    try:
        team_usecase.update_team(team)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return team


@app.delete("/teams/{team_id}")
async def delete_team(team_id: str):
    try:
        team_usecase.delete_team(team_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Team deleted successfully"}


@app.get("/teams/{team_id}", response_model=Team)
async def get_team(team_id: str):
    team = team_usecase.get_team(team_id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team
