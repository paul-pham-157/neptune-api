from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.operation_error import OperationError


T = TypeVar("T", bound="UploadMetadataDTO")


@_attrs_define
class UploadMetadataDTO:
    """
    Attributes:
        errors (Union[Unset, List['OperationError']]):
        upload_id (Union[Unset, str]):
    """

    errors: Union[Unset, List["OperationError"]] = UNSET
    upload_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        upload_id = self.upload_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if upload_id is not UNSET:
            field_dict["uploadId"] = upload_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operation_error import OperationError

        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = OperationError.from_dict(errors_item_data)

            errors.append(errors_item)

        upload_id = d.pop("uploadId", UNSET)

        upload_metadata_dto = cls(
            errors=errors,
            upload_id=upload_id,
        )

        upload_metadata_dto.additional_properties = d
        return upload_metadata_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
