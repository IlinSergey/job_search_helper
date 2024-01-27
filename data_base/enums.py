from enum import Enum


class Experience(Enum):
    noExperience = "noExperience"
    between1And3 = "between1And3"
    between3And6 = "between3And6"
    moreThan6 = "moreThan6"


class Employment(Enum):
    full = "full"
    part = "part"
    project = "project"
    probation = "probation"


class Schedule(Enum):
    fullDay = "fullDay"
    shift = "shift"
    remote = "remote"
    flexible = "flexible"
