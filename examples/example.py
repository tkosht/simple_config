# -*- coding: utf-8 -*-

from sconfig.config import Config


if __name__ == '__main__':
    cfg = Config()
    assert cfg.model1.batch_size == 2048
    assert cfg.model1.samples == 10000

    vis = cfg.get("visdom")
    assert vis.server == "0.0.0.0"
    assert vis.port == 8097

    print("OK")
