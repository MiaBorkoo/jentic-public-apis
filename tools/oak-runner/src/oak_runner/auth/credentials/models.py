from dataclasses import dataclass, field
from typing import Dict, Any, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from oak_runner.auth_parser.models import AuthValue, RequestAuthValue, SecurityScheme

# Core data structures
@dataclass
class Credential:
    """Container object that groups together all information related to a single
credential while it passes through the oak-runner pipeline.

The instance is created early by the credentials provider with a unique
`id` and optional free-form `metadata`.  Subsequent pipeline stages
(transform, validate, etc.) enrich the same instance in place instead of
returning new structures, which keeps the data flow simple and avoids
excessive object creation.

Attributes
----------
id: str
    Unique identifier for the credential
metadata: Dict[str, Any]
    Arbitrary auxiliary data coming from the provider. Can include issuer
    information, requested scopes, location hints, etc.
auth_value: AuthValue | None
    Normalised credential value as it appears in the OpenAPI document.
request_auth_value: RequestAuthValue | None
    Credential value formatted for direct injection into an outgoing HTTP
    request (e.g., header, query param, cookie).
security_scheme: SecurityScheme | None
    The OpenAPI `SecurityScheme` object that this credential fulfils.
"""
    id: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    # Fields that are populated by the provider and/or transformer
    auth_value: Union["AuthValue", None] = None
    request_auth_value: Union["RequestAuthValue", None] = None
    security_scheme: Union["SecurityScheme", None] = None
