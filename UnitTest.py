import unittest
import fact
    
    class TestFactorialMethods(unittest.TestCase):
    
        def test_normal_values(self):
            self.assertEqual(fact(0), 1)
            self.assertEqual(fact(5), 120)
            self.assertEqual(fact(10), 3628800)
            
        def test_except_ValueError(self):            
            with self.assertRaises(ValueError):
                fact(-4)
            with self.assertRaises(ValueError):
                fact(-111)
            with self.assertRaises(ValueError):
                fact(-987654321)
                
        def test_except_TypeError(self):            
            with self.assertRaises(TypeError):
                fact(0.5)
            with self.assertRaises(TypeError):
                fact('hello')
            with self.assertRaises(TypeError):
                fact([1,2,3,4])
