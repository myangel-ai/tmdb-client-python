# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ImageRetrieveResponse", "Poster"]


class Poster(BaseModel):
    aspect_ratio: Optional[float] = None

    file_path: Optional[str] = None

    height: Optional[int] = None

    iso_639_1: Optional[str] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None

    width: Optional[int] = None


class ImageRetrieveResponse(BaseModel):
    id: Optional[int] = None

    posters: Optional[List[Poster]] = None
