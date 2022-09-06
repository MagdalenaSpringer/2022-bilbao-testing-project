
""" @pytest.make.parametrize(
    "x, r, answer",
    [
        (0.1,2.2,0.198),
        (0.2,3.4,0.544),
        (0.75,1.7,0.31875),
    ]
) """
import numpy as np
from logfun import logfun

def test_conftest(random_state):
    
    r = 1.5
    l = 100
    x_val = []

    for i in np.arange(1,10):
        x = random_state.rand()
        output = logfun(x,r,l)
        assert np.isclose(output, 1/3)

        x_val += [x-1]
    return x_val



def test_chaos(random_state):
    r = 3.8
    l = 100000
    x = random_state.rand()
    output = logfun(x,r,l)
    assert np.all(output >= 0.0)
    assert np.all(output <= 1.0)
    #assert min(np.abs(np.diff(output[-1000:]))) >1000



