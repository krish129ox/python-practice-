class StateMachine:
    def __init__(self, initial):
        self.state = initial
        self.transitions = {}
    def add_transition(self, from_state, event, to_state):
        self.transitions[(from_state, event)] = to_state
    def trigger(self, event):
        key = (self.state, event)
        if key in self.transitions:
            self.state = self.transitions[key]
        return self.state