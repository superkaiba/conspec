
class Conspec:
    def __init__(
            self, 
            n_prototypes,
            buffer,
            reward_mode='sparse',
            ):
        self.buffer = buffer

    def get_prototypes(self):
        '''
        Returns current prototypes
        '''

    def train_prototypes(self):
        '''
        Trains the prototypes
        '''
    
    def get_intrinsic_reward(self, trajectory):
        '''
        Returns the intrinsic reward
        '''