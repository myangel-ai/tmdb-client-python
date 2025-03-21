# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .movies import (
    MoviesResource,
    AsyncMoviesResource,
    MoviesResourceWithRawResponse,
    AsyncMoviesResourceWithRawResponse,
    MoviesResourceWithStreamingResponse,
    AsyncMoviesResourceWithStreamingResponse,
)
from ...types import keyword_search_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.keyword_search_response import KeywordSearchResponse
from ...types.keyword_retrieve_response import KeywordRetrieveResponse

__all__ = ["KeywordsResource", "AsyncKeywordsResource"]


class KeywordsResource(SyncAPIResource):
    @cached_property
    def movies(self) -> MoviesResource:
        return MoviesResource(self._client)

    @cached_property
    def with_raw_response(self) -> KeywordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return KeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return KeywordsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        keyword_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeywordRetrieveResponse:
        """
        Details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/keyword/{keyword_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordRetrieveResponse,
        )

    def search(
        self,
        *,
        query: str,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeywordSearchResponse:
        """
        Search for keywords by their name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/search/keyword",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "page": page,
                    },
                    keyword_search_params.KeywordSearchParams,
                ),
            ),
            cast_to=KeywordSearchResponse,
        )


class AsyncKeywordsResource(AsyncAPIResource):
    @cached_property
    def movies(self) -> AsyncMoviesResource:
        return AsyncMoviesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKeywordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncKeywordsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        keyword_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeywordRetrieveResponse:
        """
        Details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/keyword/{keyword_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordRetrieveResponse,
        )

    async def search(
        self,
        *,
        query: str,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeywordSearchResponse:
        """
        Search for keywords by their name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/search/keyword",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "page": page,
                    },
                    keyword_search_params.KeywordSearchParams,
                ),
            ),
            cast_to=KeywordSearchResponse,
        )


class KeywordsResourceWithRawResponse:
    def __init__(self, keywords: KeywordsResource) -> None:
        self._keywords = keywords

        self.retrieve = to_raw_response_wrapper(
            keywords.retrieve,
        )
        self.search = to_raw_response_wrapper(
            keywords.search,
        )

    @cached_property
    def movies(self) -> MoviesResourceWithRawResponse:
        return MoviesResourceWithRawResponse(self._keywords.movies)


class AsyncKeywordsResourceWithRawResponse:
    def __init__(self, keywords: AsyncKeywordsResource) -> None:
        self._keywords = keywords

        self.retrieve = async_to_raw_response_wrapper(
            keywords.retrieve,
        )
        self.search = async_to_raw_response_wrapper(
            keywords.search,
        )

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithRawResponse:
        return AsyncMoviesResourceWithRawResponse(self._keywords.movies)


class KeywordsResourceWithStreamingResponse:
    def __init__(self, keywords: KeywordsResource) -> None:
        self._keywords = keywords

        self.retrieve = to_streamed_response_wrapper(
            keywords.retrieve,
        )
        self.search = to_streamed_response_wrapper(
            keywords.search,
        )

    @cached_property
    def movies(self) -> MoviesResourceWithStreamingResponse:
        return MoviesResourceWithStreamingResponse(self._keywords.movies)


class AsyncKeywordsResourceWithStreamingResponse:
    def __init__(self, keywords: AsyncKeywordsResource) -> None:
        self._keywords = keywords

        self.retrieve = async_to_streamed_response_wrapper(
            keywords.retrieve,
        )
        self.search = async_to_streamed_response_wrapper(
            keywords.search,
        )

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithStreamingResponse:
        return AsyncMoviesResourceWithStreamingResponse(self._keywords.movies)
