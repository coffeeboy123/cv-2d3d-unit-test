import os
import sys
import numpy as np
import pytest

sys.path.append(os.path.abspath("src"))

from depth_processing import generate_depth_map, generate_point_cloud


def test_generate_depth_map():
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    gray, depth_map = generate_depth_map(image)

    assert gray.shape == (100, 100)
    assert depth_map.shape == image.shape
    assert isinstance(depth_map, np.ndarray)


def test_generate_point_cloud():
    gray = np.zeros((100, 100), dtype=np.uint8)
    points_3d = generate_point_cloud(gray)

    assert points_3d.shape == (100, 100, 3)
    assert isinstance(points_3d, np.ndarray)


def test_generate_depth_map_none():
    with pytest.raises(ValueError):
        generate_depth_map(None)