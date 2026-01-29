from contextvars import ContextVar

file = ContextVar("file", default=None)
data = ContextVar("data", default=None)