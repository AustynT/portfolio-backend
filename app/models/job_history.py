from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, validates
from app.models.base_model import BaseModel

# Constants for column lengths
MAX_LOCATION_LENGTH = 255
MAX_DESCRIPTION_LENGTH = 1000

class JobHistory(BaseModel):
    """
    Represents a user's job history, including location, description, and duration.
    """
    __tablename__ = "job_histories"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        doc="Primary key identifier for the job history."
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        index=True,
        doc="Foreign key linking to the User model."
    )

    location = Column(
        String(MAX_LOCATION_LENGTH),
        nullable=False,
        index=True,
        doc=f"The location of the job (max {MAX_LOCATION_LENGTH} characters)."
    )

    description = Column(
        String(MAX_DESCRIPTION_LENGTH),
        nullable=False,
        doc=f"Description of the job (max {MAX_DESCRIPTION_LENGTH} characters)."
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
        index=True,
        doc="Indicates whether the job is currently active."
    )

    start_date = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
        doc="The start date of the job."
    )

    end_date = Column(
        DateTime,
        nullable=True,
        doc="The end date of the job. Nullable for active jobs."
    )

    user = relationship(
        "User",
        back_populates="job_histories",
        doc="Relationship linking to the User model."
    )

    projects = relationship(
        "Project",
        back_populates="job_history",
        doc="Relationship linking to the Project model."
    )

    skills = relationship(
        "Skill",
        secondary="job_history_skills",
        back_populates="job_histories",
        doc="Many-to-Many relationship linking to the Skill model."
    )

    @property
    def is_current(self):
        """
        Determine if the job is still active based on the end_date.

        Returns:
            bool: True if the job is active, False otherwise.
        """
        return self.end_date is None or self.end_date > datetime.now(timezone.utc)
