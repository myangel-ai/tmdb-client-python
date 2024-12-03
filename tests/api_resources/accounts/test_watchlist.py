# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.accounts import WatchlistCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatchlist:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: TmdbClient) -> None:
        watchlist = client.accounts.watchlist.create(
            account_id=0,
            raw_body="RAW_BODY",
        )
        assert_matches_type(WatchlistCreateResponse, watchlist, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: TmdbClient) -> None:
        watchlist = client.accounts.watchlist.create(
            account_id=0,
            raw_body="RAW_BODY",
            session_id="session_id",
        )
        assert_matches_type(WatchlistCreateResponse, watchlist, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: TmdbClient) -> None:
        response = client.accounts.watchlist.with_raw_response.create(
            account_id=0,
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = response.parse()
        assert_matches_type(WatchlistCreateResponse, watchlist, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: TmdbClient) -> None:
        with client.accounts.watchlist.with_streaming_response.create(
            account_id=0,
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = response.parse()
            assert_matches_type(WatchlistCreateResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWatchlist:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTmdbClient) -> None:
        watchlist = await async_client.accounts.watchlist.create(
            account_id=0,
            raw_body="RAW_BODY",
        )
        assert_matches_type(WatchlistCreateResponse, watchlist, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        watchlist = await async_client.accounts.watchlist.create(
            account_id=0,
            raw_body="RAW_BODY",
            session_id="session_id",
        )
        assert_matches_type(WatchlistCreateResponse, watchlist, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.accounts.watchlist.with_raw_response.create(
            account_id=0,
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist = await response.parse()
        assert_matches_type(WatchlistCreateResponse, watchlist, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.accounts.watchlist.with_streaming_response.create(
            account_id=0,
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist = await response.parse()
            assert_matches_type(WatchlistCreateResponse, watchlist, path=["response"])

        assert cast(Any, response.is_closed) is True
