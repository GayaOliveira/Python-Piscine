from typing import Optional
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=6, max_length=6)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    last_maintenance = station.last_maintenance.strftime("%d/%m/%Y")
    print(f"Last Maintenance: {last_maintenance}")
    if (station.is_operational):
        print("Status: Operational")
    else:
        print("Status: Inactive")
    if (station.notes):
        print(f"Notes: {station.notes}")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station1 = SpaceStation(
            station_id="SS0001",
            name="Estação Primeira de Mangueira",
            crew_size="18",
            power_level="91.3",
            oxygen_level="95.8",
            last_maintenance="2026-04-05T14:30:00",
            is_operational="True",
            notes="This is a very special space station"
        )
        display_station(station1)
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            print(error['msg'])
    print("\n========================================")
    try:
        station2 = SpaceStation(
            station_id="SS0002",
            name="Saens Peña",
            crew_size="5",
            power_level="91.2",
            oxygen_level="90.8",
            last_maintenance="2026-04-20T18:30:00",
            is_operational="False"
        )
        display_station(station2)
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            print(error['msg'])
    print("\n========================================")
    try:
        station3 = SpaceStation(
            station_id="SS0003",
            name="Central do Brasil",
            crew_size=30,
            power_level=67.67,
            oxygen_level=4.20,
            last_maintenance="2025-11-07T18:30:00"
        )
        display_station(station3)
    except ValidationError as err:
        print("Expected validation error:")
        for error in err.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()


"""
Roteiro:
python3 -m venv ../venv
source ../venv/bin/activate
pip install pydantic
python3 space_station.py
deactivate

# =====================================================================
# EXERCISE 0 CHEATSHEET (SPACE STATION) - PYDANTIC FUNDAMENTALS
# =====================================================================
#
# Detailed explanation of new concepts introduced in this exercise:
#
# 1. Pydantic BaseModel:
#   In traditional Python, if we define 'crew_size: int', the language doesn't
#   prevent someone from putting 'crew_size = "twenty"', causing a crash later.
#   By inheriting from `BaseModel`, we transform a simple class into a strict
#   "validation border".
#   -> If a value arrives with the wrong type (e.g., a "10" string passed to an
#      int field), Pydantic AUTOMATICALLY converts it to an integer.
#   -> If the value cannot be converted (e.g., "twenty"), Pydantic intercepts
#      the data and gracefully raises a `ValidationError` before the bad data
#      infiltrates your program.

personal note: it's help to don't have the work to create a lot of try and
excepts with personalized error menssages since it already have it built

#
# 2. Pydantic Field() & Constraints:
#   Just knowing the "Type" of data isn't enough in the real world. A crew size
#   is an integer, but it can't be negative! The `Field()` function adds
#   granular business rules to our plain types.
#   -> Numbers (int, float): We use `ge` (greater or equal) and `le` (less
#      or equal) to establish boundaries.
#   -> Strings (str): We use `min_length` and `max_length` to prevent empty
#      names or absurdly long texts that could break a database.
#
# 3. Optional vs Default values:
#   -> `is_operational: bool = True`: If the user initializing this class omits
#      this field, Pydantic automatically fills it with True.
#   -> `Optional[str]`: Implies the field might be entirely absent. In modern
#      Pydantic, we MUST explicitly say `default=None` inside the Field() if
#      a field is Truly optional, otherwise Pydantic will still force the user
#      to pass `None` during initialization.
#
# 4. ValidationError Exception:
#    When we feed a BaseModel with parameters that violate the Field boundaries
#    (e.g., crew_size = 25), Pydantic raises a `ValidationError`.
#    We catch it using a `try / except ValidationError` block. This prevents
#    the program from experiencing a fatal crash, and instead, we can print
#    the exact reason why the data was rejected and continue execution.
# =====================================================================
"""
