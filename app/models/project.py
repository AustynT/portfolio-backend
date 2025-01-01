from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel

class Project(BaseModel):
    """
    Represents a project within a user's job history or personal portfolio.
    """
    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        doc="Primary key identifier for the project."
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        doc="Foreign key linking to the User model."
    )

    job_history_id = Column(
        Integer,
        ForeignKey("job_histories.id"),
        nullable=True,
        doc="Foreign key linking to the JobHistory model."
    )

    name = Column(
        String(150),
        nullable=False,
        doc="The name of the project."
    )

    description = Column(
        Text,
        nullable=True,
        doc="Optional description of the project."
    )

    start_date = Column(
        DateTime,
        nullable=False,
        doc="Start date of the project."
    )

    end_date = Column(
        DateTime,
        nullable=True,
        doc="Optional end date of the project."
    )

    user = relationship(
        "User",
        back_populates="projects",
        doc="Relationship linking to the User model."
    )

    job_history = relationship(
        "JobHistory",
        back_populates="projects",
        doc="Relationship linking to the JobHistory model."
    )

    skills = relationship(
        "Skill",
        secondary="project_skills",
        back_populates="projects",
        doc="Many-to-Many relationship linking to the Skill model."
    )
