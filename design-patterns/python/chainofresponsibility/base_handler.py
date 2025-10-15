from .request import Request
from .request_handler import RequestHandler


class BaseHandler(RequestHandler):
    def __init__(self):
        self._next: RequestHandler = None

    def set_next(self, next_handler: RequestHandler) -> None:
        self._next = next_handler

    def handle(self, request: Request) -> None:
        pass

    def _forward(self, request: Request) -> None:
        if self._next is not None:
            self._next.handle(request)
