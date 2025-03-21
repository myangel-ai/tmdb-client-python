# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ListRetrieveResponse", "Result"]


class Result(BaseModel):
    id: Optional[int] = None

    description: Optional[str] = None

    favorite_count: Optional[int] = None

    iso_639_1: Optional[str] = None

    item_count: Optional[int] = None

    list_type: Optional[str] = None

    name: Optional[str] = None

    poster_path: Optional[object] = None


class ListRetrieveResponse(BaseModel):
    id: Optional[int] = None

    page: Optional[int] = None

    results: Optional[List[Result]] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None
