class ErrorPersonalizado(Exception):
    def __init__(self,mensage: str):
        super().__init__(mensage)
