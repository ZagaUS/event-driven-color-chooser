import pytest
import handlers.rgbHandler as h

def testRgb():
    '''Test rgb handler.'''
    event = {'dummy': 'data'}
    rgbResp = h.rgb(event, {})
    
    assert rgbResp.get('statusCode') == 200