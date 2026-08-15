import unittest
from open_source_portfolio_generator import generate,probe
class Tests(unittest.TestCase):
 def test_public(self):self.assertTrue(generate({"repositories":[{"name":"x","visibility":"public"}]})["ok"])
 def test_private_blocked(self):self.assertFalse(generate({"repositories":[{"name":"x","visibility":"private"}]})["ok"])
 def test_duplicate(self):self.assertFalse(generate({"repositories":[{"name":"x","visibility":"public"},{"name":"x","visibility":"public"}]})["ok"])
 def test_probe(self):self.assertTrue(probe()["ok"])
if __name__=="__main__":unittest.main()
