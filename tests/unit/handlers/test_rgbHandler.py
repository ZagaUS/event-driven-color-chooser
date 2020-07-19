import pytest
import handlers.rgbHandler as h

def test_rgb():
    '''Test rgb handler.'''
    event = {'dummy': 'data'}
    rgbResp = h.rgb(event, {})
    
    assert rgbResp.get('statusCode') == 200