# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.person.latest_retrieve_response import LatestRetrieveResponse

__all__ = ["LatestResource", "AsyncLatestResource"]


class LatestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LatestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return LatestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LatestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return LatestResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatestRetrieveResponse:
        """Get the newest created person.

        This is a live response and will continuously
        change.
        """
        return self._get(
            "/3/person/latest",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LatestRetrieveResponse,
        )


class AsyncLatestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLatestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLatestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLatestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncLatestResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatestRetrieveResponse:
        """Get the newest created person.

        This is a live response and will continuously
        change.
        """
        return await self._get(
            "/3/person/latest",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LatestRetrieveResponse,
        )


class LatestResourceWithRawResponse:
    def __init__(self, latest: LatestResource) -> None:
        self._latest = latest

        self.retrieve = to_raw_response_wrapper(
            latest.retrieve,
        )


class AsyncLatestResourceWithRawResponse:
    def __init__(self, latest: AsyncLatestResource) -> None:
        self._latest = latest

        self.retrieve = async_to_raw_response_wrapper(
            latest.retrieve,
        )


class LatestResourceWithStreamingResponse:
    def __init__(self, latest: LatestResource) -> None:
        self._latest = latest

        self.retrieve = to_streamed_response_wrapper(
            latest.retrieve,
        )


class AsyncLatestResourceWithStreamingResponse:
    def __init__(self, latest: AsyncLatestResource) -> None:
        self._latest = latest

        self.retrieve = async_to_streamed_response_wrapper(
            latest.retrieve,
        )
