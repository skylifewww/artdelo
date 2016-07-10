from iosDevCourse.core.test import TestCase
from iosDevCourse.users.factories import UserFactory


class TestExample(TestCase):

    def test_example(self):
        UserFactory()
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
