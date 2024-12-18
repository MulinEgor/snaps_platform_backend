from api.team_members.repository import TeamMemberRepository
from api.team_members.service import TeamMemberService


service = TeamMemberService(TeamMemberRepository())


def get_team_member_service():
    return service
