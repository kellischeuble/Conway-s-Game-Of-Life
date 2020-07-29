import random


class Cell():
    # change this size to alter tthe size of the cells
    def __init__(self, size=20):
        self._status = "Dead"
        self.size = size
    
    def init_random_state(self, seed="Random"):
        """
        """
        if seed == "Random":
            # want ~40% Alive.. 
            states = ["Dead", "Alive", "Dead", "Alive", "Dead",]
            self._status = random.choice(states)

    def set_dead(self):
        """
        """
        self._status = "Dead"

    def set_alive(self):
        """
        """
        self._status = "Alive"

    def is_alive(self):
        """
        """
        if self._status == "Alive":
            return True
        return False

    def get_print_character(self):
        """
        """
        if self.is_alive():
            return "X"
        return " "