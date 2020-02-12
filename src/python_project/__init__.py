"""A Python project."""
try:
    from importlib.metadata import version  # type: ignore
except ImportError:
    from importlib_metadata import version, PackageNotFoundError  # type: ignore

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
