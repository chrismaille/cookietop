"""Read SAM template.yml file.

All AWS custom tags formats, if used,
will return literal string.
"""
from pathlib import Path

import yaml


class Ref(yaml.YAMLObject):
    yaml_tag = "!Ref"

    def __init__(self, val):
        self.val = val

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(node.value)


class GetAtt(yaml.YAMLObject):
    yaml_tag = "!GetAtt"

    def __init__(self, val):
        self.val = val

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(node.value)


class Sub(yaml.YAMLObject):
    yaml_tag = "!Sub"

    def __init__(self, val):
        self.val = val

    @classmethod
    def from_yaml(cls, loader, node):
        return cls(node.value)


def get_sam_data():
    template_path = Path().cwd().joinpath("template.yml")
    with open(str(template_path), "r") as file:
        sam = yaml.load(file, Loader=yaml.FullLoader)
    return sam
