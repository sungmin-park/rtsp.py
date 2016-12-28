from rtsp import client


def test_options():
    assert client.options('rtsp://127.0.0.1:8554/mpeg4ESVideoTest') == \
           ['OPTIONS', 'DESCRIBE', 'SETUP', 'TEARDOWN', 'PLAY', 'PAUSE', 'GET_PARAMETER', 'SET_PARAMETER']
