from http import HTTPStatus
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
    cast,
)

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.report_metadata_list_dto import ReportMetadataListDTO
from ...types import (
    UNSET,
    Response,
    Unset,
)


def _get_kwargs(
    *,
    project_identifier: str,
    report_ids: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["projectIdentifier"] = project_identifier

    json_report_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(report_ids, Unset):
        json_report_ids = report_ids

    params["reportIds"] = json_report_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/leaderboard/v1/reports/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ReportMetadataListDTO]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReportMetadataListDTO.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.REQUEST_TIMEOUT:
        response_408 = cast(Any, None)
        return response_408
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ReportMetadataListDTO]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    project_identifier: str,
    report_ids: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, ReportMetadataListDTO]]:
    """List reports' metadata

    Args:
        project_identifier (str):
        report_ids (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReportMetadataListDTO]]
    """

    kwargs = _get_kwargs(
        project_identifier=project_identifier,
        report_ids=report_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    project_identifier: str,
    report_ids: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, ReportMetadataListDTO]]:
    """List reports' metadata

    Args:
        project_identifier (str):
        report_ids (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReportMetadataListDTO]
    """

    return sync_detailed(
        client=client,
        project_identifier=project_identifier,
        report_ids=report_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    project_identifier: str,
    report_ids: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, ReportMetadataListDTO]]:
    """List reports' metadata

    Args:
        project_identifier (str):
        report_ids (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReportMetadataListDTO]]
    """

    kwargs = _get_kwargs(
        project_identifier=project_identifier,
        report_ids=report_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    project_identifier: str,
    report_ids: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, ReportMetadataListDTO]]:
    """List reports' metadata

    Args:
        project_identifier (str):
        report_ids (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReportMetadataListDTO]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_identifier=project_identifier,
            report_ids=report_ids,
        )
    ).parsed
