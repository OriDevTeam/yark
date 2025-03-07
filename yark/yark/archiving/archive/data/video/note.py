"""User note-taking/journaling to record interesting parts of videos using a timestamp"""
# Standard Imports
from __future__ import annotations
from uuid import uuid4
from typing import Optional, TYPE_CHECKING, Any
from dataclasses import dataclass, field

# Local Imports
if TYPE_CHECKING:
    from .data import Video

# External Imports


def _id_generator() -> str:
    """Generates an identifier for new notes"""
    return str(uuid4())


@dataclass
class Note:
    parent: Video
    timestamp: int
    title: str
    body: Optional[str] = None
    id: str = field(default_factory=_id_generator)


def from_archive_o(parent: Video, element: dict[str, Any]) -> Note:
    """Loads existing note object dict from an archive"""
    return Note(
        parent,
        element["timestamp"],
        element["title"],
        element["body"],
        element["id"],
    )


def _to_archive_o(self) -> dict[str, Any]:
    """Converts note to it's object dict for archival"""
    return {
        "id": self.id,
        "timestamp": self.timestamp,
        "title": self.title,
        "body": self.body,
    }
