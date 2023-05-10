import getpass
import json
import logging
import os
import random
from functools import lru_cache
from pathlib import Path
import jinja2
ENVS = ["dev", "prod"]

#: JSON config files under confluent/config/{{env}}/
CONFIGS = [
    "github",
    "kiosk",
    "paths",
    "patterns",
    "projects",
    "test-owners",
    "versions",
]

#: Default env and configs for load configs
DEFAULT_ENV = "dev"
DEFAULT_CONFIG = "projects"

#: Prod user for projects.json
PROD_USER = "confluentinc"
@lru_cache()
def load_config(env_name=DEFAULT_ENV, config_name=DEFAULT_CONFIG, fs_root=None):

    if env_name not in ENVS:
        raise ValueError(
            "'{}' isn't an env name. Try one of: {}".format(env_name, ", ".join(ENVS))
        )

    if config_name not in CONFIGS:
        raise ValueError(
            "'{}' isn't a config name. Try one of: {}".format(
                config_name, ", ".join(CONFIGS)
            )
        )

    if fs_root:
        loader = jinja2.FileSystemLoader(str(Path(fs_root) / env_name))
    else:
        loader = jinja2.PackageLoader("confluent.config", env_name)

    env = jinja2.Environment(loader=loader)
    config_file = "{}.json".format(config_name)
    template = env.get_template(config_file)
    default_config = json.loads(template.render(user="maxzheng"))
    return default_config


