# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.guest_sessions.rated import TvListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTv:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        tv = client.guest_sessions.rated.tv.list(
            guest_session_id="guest_session_id",
        )
        assert_matches_type(TvListResponse, tv, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TmdbClient) -> None:
        tv = client.guest_sessions.rated.tv.list(
            guest_session_id="guest_session_id",
            language="language",
            page=0,
            sort_by="created_at.asc",
        )
        assert_matches_type(TvListResponse, tv, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.guest_sessions.rated.tv.with_raw_response.list(
            guest_session_id="guest_session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tv = response.parse()
        assert_matches_type(TvListResponse, tv, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.guest_sessions.rated.tv.with_streaming_response.list(
            guest_session_id="guest_session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tv = response.parse()
            assert_matches_type(TvListResponse, tv, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: TmdbClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guest_session_id` but received ''"):
            client.guest_sessions.rated.tv.with_raw_response.list(
                guest_session_id="",
            )


class TestAsyncTv:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        tv = await async_client.guest_sessions.rated.tv.list(
            guest_session_id="guest_session_id",
        )
        assert_matches_type(TvListResponse, tv, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        tv = await async_client.guest_sessions.rated.tv.list(
            guest_session_id="guest_session_id",
            language="language",
            page=0,
            sort_by="created_at.asc",
        )
        assert_matches_type(TvListResponse, tv, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.guest_sessions.rated.tv.with_raw_response.list(
            guest_session_id="guest_session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tv = await response.parse()
        assert_matches_type(TvListResponse, tv, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.guest_sessions.rated.tv.with_streaming_response.list(
            guest_session_id="guest_session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tv = await response.parse()
            assert_matches_type(TvListResponse, tv, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTmdbClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `guest_session_id` but received ''"):
            await async_client.guest_sessions.rated.tv.with_raw_response.list(
                guest_session_id="",
            )
