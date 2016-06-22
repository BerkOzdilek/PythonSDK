from unittest import TestCase
import ivencloud
from ivencloud import api


class TestIvencloud(TestCase):
    def test_activate(self):
        s = ivencloud.activate_device(None, None)
        self.assertTrue(s is None)

    def test_senddata(self):
        api.api_key = None
        s = ivencloud.send_data(None)
        self.assertEqual(s, [None, 2])

    def test_api_null(self):
        api.api_key = "s"
        s = ivencloud.send_data(None)
        self.assertEqual(s, [None, 1])

    def test_send_datanull(self):
        api.api_key = "s"
        s = ivencloud.send_data({})
        self.assertEqual(s, [None, 1])

    def test_setFreq(self):
        s = ivencloud.set_frequency(0)
        self.assertFalse(s)



