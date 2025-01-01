from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.database import Base

project_skills = Table(
    "project_skills",
    Base.metadata,
    Column(
        "project_id",
        Integer,
        ForeignKey("projects.id"),
        primary_key=True,
        doc="Foreign key linking to the Project model."
    ),
    Column(
        "skill_id",
        Integer,
        ForeignKey("skills.id"),
        primary_key=True,
        doc="Foreign key linking to the Skill model."
    ),
    doc="Association table linking Project to Skill."
)
