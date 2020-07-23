import pytest
import os
import src.rgbHandler as h
import unittest.mock as mock

def test_getRgb():
    event = {'dummy': 'data'}
    k = mock.patch.dict(os.environ, {"REDIS_HOST": "host", "REDIS_PORT": "1234"})
    k.start()
    rgbResp = h.getRgb(event, {})
    k.stop()
    
    assert rgbResp.get('statusCode') == 200