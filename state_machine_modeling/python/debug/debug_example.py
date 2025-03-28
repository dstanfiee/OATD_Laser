import logging
import pdb
from example import StateMachine

# Configure logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    sm = StateMachine()
    
    logging.debug(f"Initial state: {type(sm.state).__name__}")
    
    sm.on_event('to_B')
    logging.debug(f"State after 'to_B' event: {type(sm.state).__name__}")
    
    sm.on_event('to_A')
    logging.debug(f"State after 'to_A' event: {type(sm.state).__name__}")
    
    # Example of using pdb for debugging
    pdb.set_trace()
    sm.on_event('to_C')
    logging.debug(f"State after 'to_C' event: {type(sm.state).__name__}")
