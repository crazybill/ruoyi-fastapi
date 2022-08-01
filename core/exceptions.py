from fastapi import HTTPException


class MissingSessionError(Exception):
    """Excetion raised for when the user tries to access a database session before it is created."""

    def __init__(self):
        msg = """
        No session found! Either you are not currently in a request context,
        or you need to manually create a session context by using a `db` instance as
        a context manager e.g.:

        with db():
            db.session.query(User).all()
        """

        super().__init__(msg)


class SessionNotInitialisedError(Exception):
    """Exception raised when the user creates a new DB session without first initialising it."""

    def __init__(self):
        msg = """
        Session not initialised! Ensure that DBSessionMiddleware has been initialised before
        attempting database access.
        """

        super().__init__(msg)

class Error401(HTTPException):
    def __init__(self):
        status_code = 401
        detail = "登录已过期，请重新登录！"
        super().__init__(status_code = status_code, detail=detail)

class Error403(HTTPException):
    def __init__(self):
        status_code = 403
        detail = "您没有权限访问该资源！"
        
        super().__init__(status_code = status_code, detail=detail)