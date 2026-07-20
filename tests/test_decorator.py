import io
import sys
import numpy as np
import pytest
from unittest.mock import patch

from var_scout.decorator import log_local_vars
from var_scout.reporters.shape import ShapeReporter

def test_normal_func():
  @log_local_vars()
  def normal_func():
    x = np.zeros((2, 3))
  
  with patch('sys.stdout', new=io.StringIO()) as fake_out:
    normal_func()
    output = fake_out.getvalue()

  assert "Normal" in output
  assert "'x': shape=(2, 3)" in output

def test_crash_func():
  @log_local_vars()
  def crash_func():
    raise ValueError("Crashed")
  
  with patch('sys.stdout', new=io.StringIO()) as fake_out:
    with pytest.raises(ValueError) as exc_info:
      crash_func()
    output = fake_out.getvalue()
  
  assert "Test Error" in str(exc_info.value)
  assert "Exception" in output
  
def test_empty_func():
  @log_local_vars()
  def empty_func(): pass

  with patch('sys.stdout', new=io.StringIO()) as fake_out:
    empty_func()
    output = fake_out.getvalue()

  assert "Normal" in output
  assert "No local" in output
  assert "__builtins__" not in output
