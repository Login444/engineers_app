from typing import List, Optional
from app.entity.team import Team
from app.repository.team_repo import TeamRepository


class TeamUseCase:
    def __init__(self, repo: TeamRepository):
        self.repo = repo

    def create_team(self, team: Team) -> None:
        self.repo.create_team(team)

    def update_team(self, team: Team) -> None:
        if not self.repo.get_team_by_id(team.id):
            raise ValueError("Team not found")
        self.repo.update_team(team)

    def delete_team(self, team_id: str) -> None:
        self.repo.delete_team(team_id)

    def get_team(self, team_id: str) -> Optional[Team]:
        return self.repo.get_team_by_id(team_id)

    def list_teams(self) -> List[Team]:
        return self.repo.list_teams()
