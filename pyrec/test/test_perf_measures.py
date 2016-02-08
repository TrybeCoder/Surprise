"""Module for testing performance evaluation measures (RMSE, MAE...)"""

from math import sqrt
import pytest

import stats


def pred(true_r, est, u0=None):
    """Just a small tool to build a prediction with appropriate format"""
    return (u0, None, true_r, est, None)


def test_mae():

    predictions = [pred(0, 0), pred(1, 1), pred(2, 2), pred(100, 100)]
    assert stats.mae(predictions) == 0

    predictions = [pred(0, 0), pred(0, 2)]
    assert stats.mae(predictions) == abs(0 - 2) / 2

    predictions = [pred(2, 0), pred(3, 4)]
    assert stats.mae(predictions) == (abs(2 - 0) + abs(3 - 4)) / 2

def test_rmse():

    predictions = [pred(0, 0), pred(1, 1), pred(2, 2), pred(100, 100)]
    assert stats.rmse(predictions) == 0

    predictions = [pred(0, 0), pred(0, 2)]
    assert stats.rmse(predictions) == sqrt((0 - 2)**2 / 2)

    predictions = [pred(2, 0), pred(3, 4)]
    assert stats.rmse(predictions) == sqrt(((2 - 0)**2 + (3 - 4)**2) / 2)

def test_fcp():

    predictions = [pred(0, 0, u0='u1'), pred(1, 1, u0='u1'), pred(2, 2,
                   u0='u2'), pred(100, 100, u0='u2')]
    assert stats.fcp(predictions) == 1

    predictions = [pred(0, 0, u0='u1'), pred(0, 0, u0='u1')]
    with pytest.raises(ValueError):
        stats.fcp(predictions)

    predictions = [pred(0, 0, u0='u1')]
    with pytest.raises(ValueError):
        stats.fcp(predictions)

    predictions = [pred(0, 1, u0='u1'), pred(1, 0, u0='u1'), pred(2, 0.5,
                   u0='u2'), pred(0, 0.6, u0='u2')]
    assert stats.fcp(predictions) == 0
