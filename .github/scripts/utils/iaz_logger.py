import logging

from colorlog import ColoredFormatter

class IAZLogger(logging.Logger):

    def __init__(self, name: str = "IAZ Logger", level: int = logging.INFO) -> None:
        super().__init__(name, level)
        logger_format = "%(asctime)s [%(levelname)s] %(message)s"
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(ColoredFormatter(logger_format, force_color=True))
        self.addHandler(console_handler)
