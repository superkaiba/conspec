

class ConspecBuffer:
    def __init__(self, n_successes, n_failures):
        self.n_successes = n_successes
        self.n_failures = n_failures

    def add_trajectory(self, trajectory):
        '''
        Adds a trajectory to the buffer.
        If the trajectory is considered a "success", then add it to the success buffer
        If the trajectory is considered a "failure", then add it to the failure buffer
        Else discard it
        '''

    def get_successes(self):
        '''
        Returns a list of successful trajectories
        '''
    
    def get_failures(self):
        '''
        Returns a list of failed trajectories
        '''


class Buffer:
    def __init__(self, n_trajectories):
        self.n_trajectories = n_trajectories
        self.buffer = []

    def add_trajectory(self, trajectory):
        
    

