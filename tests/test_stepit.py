import glob
import os
import shutil
import time

import pytest

from stepit import default_deserialize, stepit

import logging
logging.getLogger("stepit").setLevel(logging.DEBUG)


def test_stepit_defaults():
    """Test with defaults, that a stepit-decorated function saves its result to
    cache and when args are the same, that it reads from cache instead of running again,"""
    cache_dir = ".stepit_cache"
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)

    @stepit
    def a(x):
        time.sleep(5)
        return x + 2

    start_time = time.time()
    a(5)
    elapsed_time = time.time() - start_time
    assert elapsed_time >= 5
    assert default_deserialize(f"{cache_dir}/a") == 7
