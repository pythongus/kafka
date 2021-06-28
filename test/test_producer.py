"""
Unit tests for the producer
"""
import os
from unittest.mock import MagicMock, patch
from pyprod.producer import get_data


def test_get_data():
    with patch('pyprod.producer.DATA_FILE', new='./test/data.csv') as mock_data_file:
        callback = MagicMock()
        get_data(callback)
        callback.assert_called_once()


def test_get_data_no_data_file():
    with patch('pyprod.producer.DATA_FILE', new=None) as mock_data_file, \
            patch('pyprod.producer.exit', callable=raiseError) as sys_exit:
        try:
            get_data(None)
            assert False, 'Exception not raised'
        except:
            assert True


def raiseError():
    raise Exception('Exception raised')
