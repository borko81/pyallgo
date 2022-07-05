import asyncio
import socket
from keyword import kwlist

MAX_KEYWORD_LEN = 4


names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)


async def probe(domain: str) -> tuple[str, bool]:
    loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return (domain, False)
    return (domain, True)


if __name__ == '__main__':
    result = asyncio.run(probe("https://unrealsoft.net"))
    print(result)