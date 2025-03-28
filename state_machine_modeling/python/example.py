# Intel Corporation Internal Use Only
# 
# This software is intended solely for internal use within Intel Corporation.
# Unauthorized copying or distribution of this software, via any medium, is strictly prohibited.
#
# Python Example Script

import logging
import pdb  # Python debugger
import time  # For potential timing operations
import random  # For potential random event generation

class State:
    """
    Base class for all states. Each state should inherit from this class and implement the `on_event` method.
    """
    def on_event(self, event):
        """
        Handle events that are delegated to this State.
        """
        pass

class StateA(State):
    """
    Example state A.
    """
    def on_event(self, event):
        if event == 'to_B':
            logging.info("Transitioning from StateA to StateB")
            return StateB()
        elif event == 'to_C':
            logging.info("Transitioning from StateA to StateC")
            return StateC()
        return self

class StateB(State):
    """
    Example state B.
    """
    def on_event(self, event):
        if event == 'to_A':
            logging.info("Transitioning from StateB to StateA")
            return StateA()
        elif event == 'to_C':
            logging.info("Transitioning from StateB to StateC")
            return StateC()
        return self

class StateC(State):
    """
    Example state C.
    """
    def on_event(self, event):
        if event == 'to_A':
            logging.info("Transitioning from StateC to StateA")
            return StateA()
        elif event == 'to_B':
            logging.info("Transitioning from StateC to StateB")
            return StateB()
        return self

class StateMachine:
    """
    A state machine that manages transitions between states.
    """
    def __init__(self):
        self.state = StateA()  # Initial state
        logging.info(f"Initial state: {type(self.state).__name__}")

    def on_event(self, event):
        """
        Delegate the event to the current state and update the state.
        """
        logging.debug(f"Event received: {event}")
        self.state = self.state.on_event(event)
        logging.info(f"Current state: {type(self.state).__name__}")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.DEBUG)
    
    # Example usage of the state machine
    sm = StateMachine()
    
    # Transition to StateB
    sm.on_event('to_B')
    
    # Transition back to StateA
    sm.on_event('to_A')
    
    # Transition to StateC
    sm.on_event('to_C')
    
    # Transition from StateC to StateB
    sm.on_event('to_B')
    
    # Example of using pdb for debugging
    pdb.set_trace()
    sm.on_event('to_A')
