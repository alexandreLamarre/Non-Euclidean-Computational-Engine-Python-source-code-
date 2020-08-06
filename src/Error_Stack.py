class ErrorStack:
    def __init__(self):
        self.error_str = ""
        self.stop = False

    def push_error(self, error):
        """
        (String) -> None
        """
        self.error_str += error

    def check_errors(self):
        return self.error_str

    def set_stop(self):
        self.stop = True

    def stop_exec(self):
        """ If any errors have been pushed to the stack, exit the program"""
        if self.stop:
            exit(1)
