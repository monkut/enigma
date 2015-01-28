"""
implementation of 'enigma'
"""
from itertools import cycle
import string

UPPER_ALPHABET = string.ascii_uppercase

class Rotor(object):
    
    def __init__(self, rotor_id, seq, turnover_positions=None):
        self.id = rotor_id # I, II, etc
        assert len(UPPER_ALPHABET) == len(seq)
        if turnover_positions:
            self.turnover_positions = cycle(turnover_positions)
            self.turnover_position = next(self.turnover_positions)
        else:
            self.turnover_positions = []
            self.turnover_position = None
       
        self._cycle = cycle(seq)
        self._set_mappings()
    
    def _set_mappings(self):
        seq = [self._cycle.next() for i in range(26)]
        # cycle through and assign the remaining
        self.right2left_map = dict(zip(UPPER_ALPHABET, seq))
        self.left2right_map = dict(zip(seq, UPPER_ALPHABET))    
        self.current_position = seq[0]
        
    def set_ring_position(self, start_position):
        """Set the right-setting or start position of the rotor""" 
        while self.current_position != start_position:
            self.step()
        
    def step(self):
        self._cycle.next()
        self._set_mappings()
        return self.current_position
    
    def encypher(self, letter, direction="right2left"):
        if direction == "right2left":
            e = self.right2left_map[letter]
        else:
            e = self.left2right_map[letter]
        return e
    
    
class Machine(object):
    def __init__(self):
        self.rotors = []
        self.reflector = {} # a:z letter mapping
    
    def add_rotor(self, rotor):
        self.rotors.append(rotor)
        
    
    def encipher(self, text):
        # right-most rotor changes on each letter
        # --> others ?
        for letter in text:
            # go through right to left
            for rotor in rotors:
                e = rotor.
            
            
        
        pass
        
