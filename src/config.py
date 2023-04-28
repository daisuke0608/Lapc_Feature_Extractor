import dataclasses

import yaml


@dataclasses.dataclass(frozen=True)
class Config:
    batch_size: int


def get_config(config_path):
    with open(config_path, "r") as f:
        config_dict = yaml.safe_load(f)
    config = Config(**config_dict)
    return config


