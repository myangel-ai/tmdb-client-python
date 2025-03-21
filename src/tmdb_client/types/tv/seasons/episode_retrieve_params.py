# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EpisodeRetrieveParams"]


class EpisodeRetrieveParams(TypedDict, total=False):
    series_id: Required[int]

    season_number: Required[int]

    append_to_response: str
    """comma separated list of endpoints within this namespace, 20 items max"""

    language: str
