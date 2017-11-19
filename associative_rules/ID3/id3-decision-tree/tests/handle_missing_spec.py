import unittest
from ..modules.handle_missing_spec import *

class AttributeModeTests(unittest.TestCase):
  def skip_none(self):
    data_set = [[0, 1], [0, -1], [0, 1], [0, -1], [0, 0], [0, 1], [0, None], [0, None], [0, None], [0, None], [0, None]]
    result = 1
    self.assertEqual(attribute_mode(data_set, 1), result)

  def handle_ties(self):
    data_set = [[0, 1], [0, -1], [0, 1], [0, -1]]
    result = 1 or -1
    self.assertEqual(attribute_mode(data_set, 1), result)


class AttributeMeanTests(unittest.TestCase):
  def skip_none(self):
    data_set = [[0, 0.5], [0, 0.7], [0, 0.9], [0, 0.33], [0, 0.63], [0, 0.61], [0, None], [0, None], [0, None], [0, None], [0, None]]
    result = 0.6116666666666667
    self.assertEqual(attribute_mean(data_set, 1), result)

  def handle_ties(self):
    data_set = [[0, 1], [0, -1], [0, 1], [0, -1]]
    result = 0
    self.assertEqual(attribute_mean(data_set, 1), result)


class AttributeMeanTests(unittest.TestCase):
  def handle_numerical(self):
    data_set = [[0, 0.5], [0, 0.7], [0, 0.9], [0, 0.33], [0, 0.63], [0, 0.61], [0, None], [0, None], [0, None], [0, None], [0, None]]
    attribute_metadata = [{ 'name': "winpercent", 'is_nominal': False }, { 'name': "weather", 'is_nominal': False }]
    result = [[0, 0.5], [0, 0.7], [0, 0.9], [0, 0.33], [0, 0.63], [0, 0.61], [0, 0.6116666666666667], [0, 0.6116666666666667], [0, 0.6116666666666667], [0, 0.6116666666666667], [0, 0.6116666666666667]]
    self.assertEqual(handle_missing(data_set, attribute_metadata, 1), result)

  def dont_change_complete(self):
    data_set = [[0, 1], [0, -1], [0, 1], [0, -1]]
    attribute_metadata = [{ 'name': "winpercent", 'is_nominal': False }, { 'name': "weather", 'is_nominal': True }]
    result = [[0, 1], [0, -1], [0, 1], [0, -1]]
    self.assertEqual(handle_missing(data_set, attribute_metadata, 1), result)

  def handle_nominal(self):
    data_set = [[0, 1], [0, -1], [0, 1], [0, -1], [0, 0], [0, 1], [0, None], [0, None], [0, None], [0, None], [0, None]]
    result = [[0, 1], [0, -1], [0, 1], [0, -1], [0, 0], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
    self.assertEqual(handle_missing(data_set, attribute_metadata, 1), result)


if __name__ == "__main__":
  unittest.main()