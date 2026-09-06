def normalize(value: str) -> str:
    """Collapse Unicode whitespace into single ASCII spaces."""
    return " ".join(value.split())
