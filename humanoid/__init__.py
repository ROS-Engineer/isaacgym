import os

# /home/khy/standing
LEGGED_GYM_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# /home/khy/standing/humanoid/envs
LEGGED_GYM_ENVS_DIR = os.path.join(LEGGED_GYM_ROOT_DIR, 'humanoid', 'envs')