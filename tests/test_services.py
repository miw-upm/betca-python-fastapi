import unittest

from customer_support.domain.services.complaint import ComplaintService


class TestService(unittest.TestCase):
    def setUp(self):
        self.service = ComplaintService()

    def test_read(self):
        self.assertIsNotNone(self.service.read(666))


if __name__ == '__main__':
    unittest.main()
