# sconfig (simple config)
a simple config module

# installation
```bash
pip install git+https://github.com/tkosht/simple_config.git
```

# run example
```bash
cd $(git rev-parse --show-toplevel)/examples
python example.py
```

# customization

## to customize config file
you can change the config item(name or type), or values

### for yml file
you should only change the yml file like 'examples/config/project.yml'

```bash
cd $(git rev-parse --show-toplevel)/examples
vi config/project.yml
```

### for cfg and spc file
you must only change the cfg and spc file.

```bash
cd $(git rev-parse --show-toplevel)/examples
vi config/project.cfg
```

#### to customize config spec file
you must modify the spec file like 'examples/config/project.spc'
when you changed the type of some config item in config file like 'examples/config/project.cfg'.

```bash
cd $(git rev-parse --show-toplevel)/examples
vi config/project.spc
```
