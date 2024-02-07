class Config:
    _instance = None

    def __init__(self) -> None:
        self.ANSWERS_FOLDER = "answers"
        self.RESULTS_FOLDER = "results"
        self.INPUTS_FOLDER = "inputs"
        self.RAW_FOLDER = "raw"

        self.STRIP_ARG_VALUE = "--strip"
        self.STRIP_FLAG = False

        self.PRINT_ARG_VALUE = "--print"
        self.PRINT_FLAG = False

    def __new__(cls) -> "Config":
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


config = Config()
