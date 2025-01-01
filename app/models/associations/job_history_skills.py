from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.database import Base

job_history_skills = Table(
    "job_history_skills",
    Base.metadata,
    Column(
        "job_history_id",
        Integer,
        ForeignKey("job_histories.id"),
        primary_key=True,
        doc="Foreign key linking to the JobHistory model."
    ),
    Column(
        "skill_id",
        Integer,
        ForeignKey("skills.id"),
        primary_key=True,
        doc="Foreign key linking to the Skill model."
    )
)
