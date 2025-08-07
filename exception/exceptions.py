import sys

class TradingAgentException(Exception):
    
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineon = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return f"Error occured in file_name: {self.file_name}, on line: {self.lineon}\nError Message: {self.error_message}"
    
    
if __name__ == "__main__":
    try: 
        a = 1/0
        print("It will not be executed...")
        
    except Exception as e:
        raise TradingAgentException(e, sys)