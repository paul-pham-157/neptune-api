"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
from ..... import neptune_pb
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ProtoAttributesSearchResultDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTRIES_FIELD_NUMBER: builtins.int

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProtoAttributeDefinitionDTO]:
        ...

    def __init__(self, *, entries: collections.abc.Iterable[global___ProtoAttributeDefinitionDTO] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['entries', b'entries']) -> None:
        ...
global___ProtoAttributesSearchResultDTO = ProtoAttributesSearchResultDTO

@typing.final
class ProtoAttributeDefinitionDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    type: builtins.str

    def __init__(self, *, name: builtins.str=..., type: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name', 'type', b'type']) -> None:
        ...
global___ProtoAttributeDefinitionDTO = ProtoAttributeDefinitionDTO

@typing.final
class ProtoQueryAttributesResultDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ENTRIES_FIELD_NUMBER: builtins.int
    NEXTPAGE_FIELD_NUMBER: builtins.int

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProtoQueryAttributesExperimentResultDTO]:
        ...

    @property
    def nextPage(self) -> global___ProtoNextPageDTO:
        ...

    def __init__(self, *, entries: collections.abc.Iterable[global___ProtoQueryAttributesExperimentResultDTO] | None=..., nextPage: global___ProtoNextPageDTO | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['nextPage', b'nextPage']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['entries', b'entries', 'nextPage', b'nextPage']) -> None:
        ...
global___ProtoQueryAttributesResultDTO = ProtoQueryAttributesResultDTO

@typing.final
class ProtoNextPageDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NEXTPAGETOKEN_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    nextPageToken: builtins.str
    limit: builtins.int

    def __init__(self, *, nextPageToken: builtins.str | None=..., limit: builtins.int | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_limit', b'_limit', '_nextPageToken', b'_nextPageToken', 'limit', b'limit', 'nextPageToken', b'nextPageToken']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_limit', b'_limit', '_nextPageToken', b'_nextPageToken', 'limit', b'limit', 'nextPageToken', b'nextPageToken']) -> None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_limit', b'_limit']) -> typing.Literal['limit'] | None:
        ...

    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal['_nextPageToken', b'_nextPageToken']) -> typing.Literal['nextPageToken'] | None:
        ...
global___ProtoNextPageDTO = ProtoNextPageDTO

@typing.final
class ProtoQueryAttributesExperimentResultDTO(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EXPERIMENTID_FIELD_NUMBER: builtins.int
    EXPERIMENTSHORTID_FIELD_NUMBER: builtins.int
    ATTRIBUTES_FIELD_NUMBER: builtins.int
    experimentId: builtins.str
    experimentShortId: builtins.str

    @property
    def attributes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[neptune_pb.api.v1.model.leaderboard_entries_pb2.ProtoAttributeDTO]:
        ...

    def __init__(self, *, experimentId: builtins.str=..., experimentShortId: builtins.str=..., attributes: collections.abc.Iterable[neptune_pb.api.v1.model.leaderboard_entries_pb2.ProtoAttributeDTO] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['attributes', b'attributes', 'experimentId', b'experimentId', 'experimentShortId', b'experimentShortId']) -> None:
        ...
global___ProtoQueryAttributesExperimentResultDTO = ProtoQueryAttributesExperimentResultDTO