import numpy as np


def test_can_import():
    import micromagnetictestcases
    micromagnetictestcases


def test_can_access_macrospin_solution():
    import micromagnetictestcases
    # random test point
    assert np.array([1.]) == \
        micromagnetictestcases.macrospin.solution(0.1, 1, 1, [0])


def test_can_access_domainwall_solution():
    import micromagnetictestcases
    assert np.allclose(
        micromagnetictestcases.domainwall.solution(1, 1, 1, 1),
        np.array([0.46211716]))
