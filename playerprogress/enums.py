from enum import Enum


class LiftTypes(str, Enum):
    DEADLIFT = "Deadlift"
    TRAP_BAR_DEADLIFT = "Trap Bar Deadlift"
    BACK_SQUAT = "Squat"
    FRONT_SQUAT = "Front Squat"
    BENCH_PRESS = "Bench Press"


class VelocityTypes(str, Enum):
    EXIT = "Exit"
    PITCHING = "Pitching"
    OUTFIELD = "Outfield"
    INFIELD = "Infield"
    CATCHER = "Catcher"


class TimeTypes(str, Enum):
    SIXTY_YARD_DASH = "60-yd Dash"
    THIRTY_YARD_DASH = "30-yd Dash"
    POP_TIME = "Pop"
    MILE = "Mile"


class DistanceTypes(str, Enum):
    BROAD_JUMP = "Broad Jump"
    LATERAL_HOP = "Lateral Hop"
