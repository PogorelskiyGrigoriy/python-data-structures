class CompanyError(Exception):
    """Base class for exceptions in this module."""
    pass

class EmployeeAlreadyExistsError(CompanyError):
    """Raised when an employee with the given ID already exists."""
    pass

class EmployeeNotFoundError(CompanyError):
    """Raised when an employee with the given ID cannot be found."""
    pass