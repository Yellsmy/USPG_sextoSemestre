class LexicalError(Exception):
    pass

class SemanticError(Exception):
    def __init__(self, message, location=None):
        super().__init__(message)
        self.location = location