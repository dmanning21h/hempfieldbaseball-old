from enum import Enum


class VelocityTypes(str, Enum):
    EXIT = "Exit"
    PITCHING = "Pitching"
    OUTFIELD = "Outfield"
    INFIELD = "Infield"
    CATCHER = "Catcher"
