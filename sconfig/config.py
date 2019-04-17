# -*- coding: utf-8 -*-

from configobj import ConfigObj, flatten_errors
from validate import Validator

from sconfig.item import Items

default_config = "config/project.cfg"
default_spec = "config/project.spc"


class Config(Items):
    def __init__(self, config_file=default_config, config_spec=default_spec):
        config = ConfigObj(config_file, configspec=config_spec, file_error=True)
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
        self._config = config
        self.setup(config)


if __name__ == '__main__':
    cfg = Config("../examples/config/project.cfg", "../examples/config/project.spc")
    model2 = cfg.model2
    assert model2.hidden_size == 100
    print("OK")


