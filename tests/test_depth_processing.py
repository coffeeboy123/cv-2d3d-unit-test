import os
import sys
import numpy as np
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from depth_processing import generate_depth_map


def test_generate_depth_map():
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    depth_map = generate_depth_map(image)

    assert depth_map.shape == image.shape
    assert isinstance(depth_map, np.ndarray)


def test_generate_depth_map_none():
    with pytest.raises(ValueError):
        generate_depth_map(None)