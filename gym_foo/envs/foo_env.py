import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FooEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    """
    Every environment should be derived from gym.Env and at least contain the variables observation_space and action_space 
    specifying the type of possible observations and actions using spaces.Box or spaces.Discrete.

    Example:
    >>> EnvTest = FooEnv()
    >>> EnvTest.observation_space=spaces.Box(low=-1, high=1, shape=(3,4))
    >>> EnvTest.action_space=spaces.Discrete(2)
    """

  def step(self, action):
    """
    This method is the primary interface between environment and agent.

    Paramters: 
        action: int
                the index of the respective action (if action space is discrete)

    Returns:
        output: (array, float, bool)
                information provided by the environment about its current state:
                (observation, reward, done)
    """
    pass

  def reset(self):
    """
    This method resets the environment to its initial values.

    Returns:
        observation:    array
                        the initial state of the environment
    """
    pass

  def render(self, mode='human', close=False):
    """
    This methods provides the option to render the environment's behavior to a window 
    which should be readable to the human eye if mode is set to 'human'.
    """
    pass

  def close(self):
    """
    This method provides the user with the option to perform any necessary cleanup.
    """
    pass
