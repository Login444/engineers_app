from typing import List, Optional
from app.entity.team import Team


class TeamRepository:
    def __init__(self):
        self.teams = {}

    def create_team(self, team: Team) -> None:
        self.teams[team.id] = team

    def update_team(self, team: Team) -> None:
        self.teams[team.id] = team

    def delete_team(self, team_id: str) -> None:
        if team_id in self.teams:
            del self.teams[team_id]

    def get_team_by_id(self, team_id: str) -> Optional[Team]:
        return self.teams.get(team_id)

    def list_teams(self) -> List[Team]:
        return list(self.teams.values())
