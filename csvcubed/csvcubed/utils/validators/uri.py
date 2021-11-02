"""
URI
---

pydantic validators for URIs.
"""

from pydantic import validator

from ..uri import ensure_looks_like_uri


def validate_uri(attr_name: str, is_optional: bool = False) -> classmethod:
    """
    pydantic validator to ensure that an attribute has a string value which looks like a URI.

    example usage:

    .. code-block:: python

        class SomeModel(PydanticModel):
            some_uri: str

            _some_uri_validator = validate_uri("some_uri")
    """
    return validator(attr_name, allow_reuse=True, always=not is_optional)(
        ensure_looks_like_uri
    )