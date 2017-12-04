import pytest
import hypothesis.strategies as st
from hypothesis import given
import func

class TestList:

    def test_true(self):
        assert func.dict_kv(list([],[]) == {})
    
    def test_true2(self):
        assert func.dict_kv(list(['a','b'],['1']) == {'a': '1', 'b': None})
    
    def test_true3(self):
        assert func.dict_kv(list(['a','b','c','d'],['1','2','3']) == {'a': '1', 'b': '2','c':'3','d': None})
    
    @given(st.sets(st.integers()), st.sets(st.integers()))
    def my_test_hs(keys, values):
      keys = list(keys)
      values = list(values)
      result =  func.dict_kv(keys, values)

      if len(keys) < len(values):
        values = values[0:len(keys):]
      if len(values) < len(keys):
        for i in range(len(keys) - len(values)):
            values.append(None)
            

	
	assert list(result.keys()) == keys
	assert list(result.values()) == values    
