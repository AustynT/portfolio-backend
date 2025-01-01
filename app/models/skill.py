from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel

class Skill(BaseModel):
    """
    Represents a skill that can be associated with a job history or project.
    """
    __tablename__ = "skills"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        doc="Primary key identifier for the skill."
    )

    name = Column(
        String(100),
        nullable=False,
        doc="Name of the skill."
    )

    job_histories = relationship(
        "JobHistory",
        secondary="job_history_skills",
        back_populates="skills",
        doc="Many-to-Many relationship linking to the JobHistory model."
    )

    projects = relationship(
        "Project",
        secondary="project_skills",
        back_populates="skills",
        doc="Many-to-Many relationship linking to the Project model."
    )
