import random


class Cell():
    def __init__(self):
        self._status = "Dead"
    
    def init_random_state(self, seed="Random"):
        """
        """
        if seed == "Random":
            states = ["Dead", "Alive"]
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