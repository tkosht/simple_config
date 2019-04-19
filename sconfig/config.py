# -*- coding: utf-8 -*-

import pathlib
import yaml
from configobj import ConfigObj, flatten_errors
from validate import Validator

from sconfig.item import Items

# default_config = "config/project.cfg"
# default_spec = "config/project.spc"
default_config = "config/project.yml"
default_spec = None


class ConfigLoader(object):
    def load(self):
        raise NotImplementedError()


class ConfigLoaderCfg(ConfigLoader):
    def __init__(self, config_file=default_config, config_spec=default_spec):
        assert isinstance(config_file, str)
        assert isinstance(config_spec, str) or (config_spec is None)
        self.config_file = config_file
        self.config_spec = config_spec
        self._config = None

    def load(self) -> dict:
        config = ConfigObj(self.config_file, configspec=self.config_spec, file_error=True)
        if self.config_spec is not None:
            validator = Validator()
            validated = config.validate(validator, preserve_errors=True)
            if not isinstance(validated, bool) or not validated:
                errors = []
                for (section_list, key, err_info) in flatten_errors(config, validated):
                    _s = '/'.join(section_list)
                    if key is None:
                        err = f'The following section was missing "{_s}": {err_info}'
                    else:
                        err = f'The "{key}" key in the section "{_s}" failed validation: {err_info}'
                    errors.append(err)
                raise Exception(*errors)
        assert isinstance(config, dict)
        return config


class ConfigLoaderYAML(ConfigLoader):
    def __init__(self, config_file=default_config, config_spec=default_spec):
        assert isinstance(config_file, str)
        assert isinstance(config_spec, str) or (config_spec is None)
        self.config_file = config_file
        self.config_spec = config_spec
        self._config = None

    def load(self) -> dict:
        with open(self.config_file, "r") as f:
            config = yaml.safe_load(f)
        assert isinstance(config, dict)
        return config


class Config(Items):
    loader_class = {
        ".cfg": ConfigLoaderCfg,
        ".properties": ConfigLoaderCfg,
        ".yml": ConfigLoaderYAML,
        ".yaml": ConfigLoaderYAML,
    }

    def __init__(self, config_file=default_config, config_spec=default_spec):
        assert isinstance(config_file, str)
        assert isinstance(config_spec, str) or (config_spec is None)
        self.conffig_file = config_file
        self.conffig_spec = config_spec
        p = pathlib.Path(config_file)
        params = dict(
            config_file=config_file,
            config_spec=config_spec,
        )
        loader = self.loader_class[p.suffix](**params)
        self._config = loader.load()
        self.setup(self._config)


if __name__ == '__main__':
    configs = [
        Config("examples/config/project.cfg", "examples/config/project.spc"),
        Config("examples/config/project.yml"),
    ]
    for cfg in configs:
        model2 = cfg.model2
        assert model2.train.hidden_size == 100
        train = cfg.get("train")
        assert model2.train == train
        assert id(model2.train) == id(train)
        visdom = cfg.visdom
        assert visdom.server == '0.0.0.0'
        assert visdom.port == 8097

    # without spec file, all config loaded as string
    cfg = Config("examples/config/project2.cfg", None)
    model2 = cfg.model2
    assert model2.train.hidden_size == '100'
    print("OK")


