import unittest
from example import StateMachine, StateA, StateB

class TestStateMachine(unittest.TestCase):
    def test_initial_state(self):
        sm = StateMachine()
        self.assertIsInstance(sm.state, StateA)

    def test_transition_to_B(self):
        sm = StateMachine()
        sm.on_event('to_B')
        self.assertIsInstance(sm.state, StateB)

    def test_transition_to_A(self):
        sm = StateMachine()
        sm.on_event('to_B')
        sm.on_event('to_A')
        self.assertIsInstance(sm.state, StateA)

if __name__ == '__main__':
    unittest.main()
