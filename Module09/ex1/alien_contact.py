from typing import Optional
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_id(self) -> "AlienContact":
        if self.contact_id.startswith("AC"):
            return self
        raise ValueError('Contact ID must start with "AC" (Alien Contact)')

    @model_validator(mode='after')
    def validate_physical_contact(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL \
                and not self.is_verified:
            raise ValueError("Physical contacts must be verified")
        return self

    @model_validator(mode='after')
    def validate_telepathic_contact(self) -> "AlienContact":
        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        return self

    @model_validator(mode='after')
    def check_strong_signals(self) -> "AlienContact":
        if self.signal_strength > 7.0 \
                and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        report = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contact_type=ContactType.RADIO,  # Fix mypy string-to-enum type err
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="'Greetings from Zeta Reticuli'"
        )
        print(f"ID: {report.contact_id}")
        # .value extracts the string from the Enum
        print(f"Type: {report.contact_type.value}")
        print(f"Location: {report.location}")
        print(f"Signal: {report.signal_strength}/10")
        print(f"Duration: {report.duration_minutes} minutes")
        print(f"Witnesses: {report.witness_count}")
        if report.message_received:
            print(f"Message: {report.message_received}")
    except ValidationError as error:
        print("Expected validation error:")
        for item in error.errors():
            err = str(item['msg']).split(", ")
            print(err[1])

    print("\n======================================")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            contact_type=ContactType.TELEPATHIC,  # Fix mypy string-to-enum err
            location="Roswell, New Mexico",
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=2,
            message_received="I can hear them"
        )
    except ValidationError as error:
        print("Expected validation error:")
        for item in error.errors():
            err = str(item['msg']).split(", ")
            print(err[1])

    print("\n======================================")
    try:
        AlienContact(
            contact_id="AC_2024_003",
            timestamp=datetime.now(),
            contact_type=ContactType.PHYSICAL,  # Fix mypy string-to-enum err
            location="Rio de Janeiro, Rio de Janeiro",
            signal_strength=7.5,
            duration_minutes=100,
            witness_count=90,
            message_received=""
        )
    except ValidationError as error:
        print("Expected validation error:")
        for item in error.errors():
            err = str(item['msg']).split(", ")
            print(err[1])


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
# EXERCISE 1 CHEATSHEET (ALIEN CONTACT) - CUSTOM VALIDATION & ENUMS
# =====================================================================
#
# Detailed explanation of new concepts introduced in this exercise:
#
# 1. Enums (Enumerations):
#   When a field should only accept a specific set of predefined values
#   (e.g., 'radio', 'visual', 'physical', 'telepathic'), using a pure `str`
#   is dangerous. The user could type 'mind_reading' and break our logic.
#   By inheriting from `Enum`, we restrict the available options.
#   -> Magic of Pydantic: Notice we passed the string "radio" to 'contact_type'
#      in the main function. Pydantic is smart enough to check the Enum, see
#      that "radio" is a valid option, and convert it to `ContactType.RADIO`
#      automatically!
#
# 2. @model_validator(mode='after'):
#   `Field` constraints (ge, min_length...) evaluate ONE variable at a time.
#   But what if a rule depends on the interaction between MULTIPLE variables?
#   (e.g., "If the contact is telepathic, then we need at least 3 witnesses").
#
#   Then we should use `@model_validator` decorator.
#   -> `mode='after'`: This means our custom function runs ONLY AFTER all
#      the basic `Field` checks have passed. So, when our function runs, we
#      are 100% sure that `witness_count` is already a valid integer between
#      1 and 100.
#   -> The function receives `self`, which is the fully populated model
#      instance. We can write pure Python `if` statements to enforce our
#      complex business rules.
#   -> If a rule is violated, we simply `raise ValueError("Our Message")` and
#      Pydantic handles the rest, formatting it into the ValidationError.
#   -> CRITICAL: Every custom 'after' validator MUST `return self` at the end
#      because it literally modifies and returns the final validated object.
# =====================================================================
"""
