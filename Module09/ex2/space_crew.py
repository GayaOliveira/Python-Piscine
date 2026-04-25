from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutentant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_id(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        return self

    @model_validator(mode="after")
    def check_commander_or_captain(self) -> "SpaceMission":
        present = False
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                present = True
        if not present:
            raise ValueError("Must have at least one Commander or Captain")
        return self

    @model_validator(mode="after")
    def validate_experience(self) -> "SpaceMission":
        crew: list[CrewMember] = self.crew
        experienced = 0
        if self.duration_days > 365:
            for member in crew:
                if member.years_experience >= 5:
                    experienced += 1
            if experienced / len(crew) < 0.50:
                raise ValueError(
                    "Long missions (> 365 days) need"
                    "50% experienced crew (5+ years)"
                )
        return self

    @model_validator(mode="after")
    def validate_activity(self) -> "SpaceMission":
        all_active = True
        for member in self.crew:
            if not member.is_active:
                all_active = False
        if not all_active:
            raise ValueError("All crew members must be active")
        return self


def demonstration() -> None:
    print("\n=========================================")
    try:
        sarah = CrewMember(
            member_id="C625",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=48,
            specialization="Mission Command",
            years_experience=23,
            is_active=True
        )
        john = CrewMember(
            member_id="C11015",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=40,
            specialization="Navigation",
            years_experience=16,
            is_active=True
        )
        alice = CrewMember(
            member_id="C48202",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=36,
            specialization="Engineering",
            years_experience=10,
            is_active=True
        )
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[sarah, john, alice],
            mission_status="in course",
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission1.mission_name}")
        print(f"ID: {mission1.mission_id}")
        print(f"Destination: {mission1.destination}")
        print(f"Duration: {mission1.duration_days} days")
        print(f"Budget: {mission1.budget_millions}M")
        crew: list[CrewMember] = mission1.crew
        print(f"Crew size: {len(crew)}")
        print("Crew members:")
        for member in crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )

    except ValidationError as error:
        print("Expected validation error:")
        print(error)

    print("\n=========================================")
    try:
        youssef = CrewMember(
            member_id="C518637",
            name="Youssef Connor",
            rank=Rank.CADET,
            age=28,
            specialization="Cooking",
            years_experience=3,
            is_active=True
        )
        mike = CrewMember(
            member_id="C11016",
            name="Michael Smith",
            rank=Rank.LIEUTENANT,
            age=40,
            specialization="Navigation",
            years_experience=16,
            is_active=True
        )
        susie = CrewMember(
            member_id="C48200",
            name="Susan Johnson",
            rank=Rank.OFFICER,
            age=36,
            specialization="Engineering",
            years_experience=11,
            is_active=True
        )
        mission2 = SpaceMission(
            mission_id="M2022_EARTH",
            mission_name="Earth Observation",
            destination="Earth orbit",
            launch_date=datetime.now(),
            duration_days=300,
            crew=[youssef, mike, susie],
            mission_status="finished",
            budget_millions=50.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission2.mission_name}")
        print(f"ID: {mission2.mission_id}")
        print(f"Destination: {mission2.destination}")
        print(f"Duration: {mission2.duration_days} days")
        print(f"Budget: {mission2.budget_millions}M")
        crew = mission2.crew
        print(f"Crew size: {len(crew)}")
        print("Crew members:")
        for member in crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )

    except ValidationError as error:
        print("Expected validation error:")
        print(error)

    print("\n=========================================")
    try:
        sarah = CrewMember(
            member_id="C625",
            name="S",
            rank=Rank.COMMANDER,
            age=48,
            specialization="Mission Command",
            years_experience=23,
            is_active=True
        )
        john = CrewMember(
            member_id="C11015",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=40,
            specialization="Navigation",
            years_experience=16,
            is_active=True
        )
        alice = CrewMember(
            member_id="C48202",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=36,
            specialization="Engineering",
            years_experience=10,
            is_active=True
        )
        mission3 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[sarah, john, alice],
            mission_status="in course",
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission3.mission_name}")
        print(f"ID: {mission3.mission_id}")
        print(f"Destination: {mission3.destination}")
        print(f"Duration: {mission3.duration_days} days")
        print(f"Budget: {mission3.budget_millions}M")
        crew = mission3.crew
        print(f"Crew size: {len(crew)}")
        print("Crew members:")
        for member in crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )

    except ValidationError as error:
        print("Expected validation error:")
        print(error)

    print()


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    demonstration()
