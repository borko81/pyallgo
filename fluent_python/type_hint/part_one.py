from typing import Optional, Any, Union


def show_count(count: int, word: str, plural: Optional[str] = None) -> str:
    if plural:
        return plural
    if count == 1:
        return f"1 {word}"
    count_str = str(count) if count else "no"
    return f"{count_str} {word}s"


print(show_count(10, "bird", None))


# Any typing
def double(x: Any) -> Any:
    return x * 2


def to_ord(c: Union[str, bytes]) -> int:
    return ord(c)


def tokenize(text: str) -> list[str]:
    return [chr(i).upper() for i in (filter(lambda x: x > 100, map(to_ord, text)))]


print(tokenize("borko"))
