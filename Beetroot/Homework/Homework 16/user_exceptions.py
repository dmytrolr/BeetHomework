class CustomException(Exception):
    def __init__(self, msg: str):
        # logging
        with open('logs.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(msg + '\n')
        # basic Exception init
        super().__init__(msg)
