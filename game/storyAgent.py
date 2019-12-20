import os
import time

class Clear:
    """method for clear screen"""
   

    def __init__(self):
        pass

    def clear_screen(self):
        """method for clear screen after 3 secondes """
        
        time.sleep(3)
        os.system('cls||clear')