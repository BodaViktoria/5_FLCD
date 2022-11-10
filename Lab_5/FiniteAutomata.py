class FiniteAutomata:
    def __init__(self, file_name):
        self._states = []
        self._alphabet = []
        self._transitions = []
        self._initial_state = []
        self._final_state = []
        self._file = file_name
        self.insert_finite_automata()

    def insert_finite_automata(self):
        with open(self._file, 'r') as f:
            self.split_file_content(f.readline().strip(), self._states)
            self.split_file_content(f.readline().strip(), self._alphabet)
            self.split_file_content(f.readline().strip(), self._transitions)
            self.split_file_content(f.readline().strip(), self._initial_state)
            self.split_file_content(f.readline().strip(), self._final_state)

    def split_file_content(self, content, container):
        content = content.split(" ")
        for token in content:
            container.append(token)
        if content == self._transitions:
            transitions = []
            for transition in content:
                transition = transition[1:len(transition)-1].split(",")
                transitions.append([transition[0], transition[1], transition[2]])
            self._transitions = transitions

    def is_sequence_accepted(self, sequence):
        previous_state = self._initial_state[0]
        i = 0
        while i < len(sequence):
            good_paths = self.transition_contains_state([previous_state, None, sequence[i]])
            if len(good_paths) == 0:
                return False
            elif len(good_paths) == 1:
                previous_state = good_paths[0][1]
            else:
                print(good_paths)
                print("Not a deterministic finite automata!")
                return False
            i += 1
        if previous_state not in self._final_state:
            return False
        return True

    def transition_contains_state(self, state):
        good_paths = []
        for transition in self._transitions:
            if transition[0] == state[0] and transition[2] == state[2]:
                good_paths.append(transition)
        return good_paths

    def __str__(self):
        return "States: " + str(self._states) + '\n' + \
                "Alphabet: " + str(self._alphabet) + '\n' + \
                "Transitions: " + str(self._transitions) + '\n' + \
                "Initial state: " + str(self._initial_state) + '\n' + \
                "Final states: " + str(self._final_state)
