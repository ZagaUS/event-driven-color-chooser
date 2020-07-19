import pytest
import handlers.rgbHandler as h

def test_getRgb():
    '''Test rgb handler.'''
    event = {'dummy': 'data'}
    rgbResp = h.getRgb(event, {})
    
    assert rgbResp.get('statusCode') == 200