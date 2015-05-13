import os
import py
from py._path.local import LocalPath
from tox import hookimpl
from tox.config import TestenvConfig


class PathFixer(object):
    def __init__(self, old_path, new_path):
        self.old_path = old_path
        self.new_path = new_path

    def fix(self, obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, LocalPath) and self.old_path in str(v):
                    obj[k] = self.replace(v)
                elif isinstance(v, TestenvConfig):
                    self.fix(v)
                elif isinstance(v, dict):
                    self.fix(v)
        else:
            for attr_name in dir(obj):
                if attr_name.startswith("__"):
                    continue
                attr = getattr(obj, attr_name)
                if isinstance(attr, LocalPath) and self.old_path in str(attr):
                    try:
                        setattr(obj, attr_name, self.replace(attr))
                    except AttributeError:
                        # Can't set properties, etc.
                        pass
                elif isinstance(attr, TestenvConfig):
                    self.fix(attr)
                elif isinstance(attr, dict):
                    self.fix(attr)

    def replace(self, item):
        return py.path.local(str(item).replace(self.old_path, self.new_path))


@hookimpl
def tox_configure(config):
    project_name = config.toxinipath.dirpath().basename
    new_workdir = py.path.local(
        os.environ.get('TOXWORKDIRBASE', os.path.expanduser("~/.cache/tox/"))
    ).join(project_name)

    path_fixer = PathFixer(str(config.toxworkdir), str(new_workdir))
    path_fixer.fix(config)
