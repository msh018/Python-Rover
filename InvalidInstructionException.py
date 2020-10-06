class InvalidInstructionException(Exception):
    """ Exception raised when an invalid direction instruction is read
        Attributes:
            expression -- input expression in which the error occured
            message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message