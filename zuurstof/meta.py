import os
import warnings


class ZuurstofWarning(Warning):
    """Zuurstof custom warning class."""


def warn(
    message,
    stacklevel=1,
    source=None,
    *,
    skip_file_prefixes=(),
):
    try:
        skip_file_prefixes = (
            os.path.dirname(__file__),
            *skip_file_prefixes,
        )
        return warnings.warn(
            message,
            category=ZuurstofWarning,
            stacklevel=stacklevel,
            source=source,
            skip_file_prefixes=skip_file_prefixes,
        )
    except TypeError:
        # Because Python v3.11 had no skip_file_prefixes kwarg
        # This part can be removed once v3.11 is no longer supported
        return warnings.warn(
            message,
            category=ZuurstofWarning,
            stacklevel=stacklevel,
            source=source,
        )
