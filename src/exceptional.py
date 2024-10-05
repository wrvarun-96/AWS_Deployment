import sys
import logging

# Define a function to capture detailed error message
def error_message_details(error, error_detail: sys):
    """
    Captures detailed error messages with the file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()  # Get traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name
    error_message = f"Error occurred in script: [{file_name}], at line [{exc_tb.tb_lineno}], with error message: [{str(error)}]"
    return error_message

# Define a custom exception class to handle errors
class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message

