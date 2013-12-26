# coding=utf-8
""" Environment Config.

    Diffrent environment have diffrent configurations.
    You might want to change the configurations depending on the application
    environment.

    What you should do?
      1. Copy the env_config.sample.py file to env_config.py!
      2. Config the configurations by your environment.
"""


# environment (production, testing, development)
ENV = ''

# Application directory
APP_DIR = '/your/application/directory'

# Application base url
APP_BASE_URL = ''

# Application host
APP_HOST = ''
APP_PORT = 5000

# In order to use sessions you have to set a secret key.
APP_SECRET_KEY = '123456'

# The APPKey alloted by sina open platform.
SINA_APP_KEY = ''
# The APPSecret alloted by sina open platform.
SINA_APP_SECRET = ''

# The APIKey alloted by douban open platform.
DOUBAN_APP_KEY = ''
# The Secret alloted by douban open platform.
DOUBAN_APP_SECRET = ''
