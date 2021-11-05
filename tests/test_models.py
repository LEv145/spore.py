import unittest

from models import Stats


class TestModels(unittest.TestCase):
    def test_stats(self):
        self.assertEqual(
            Stats(total_uploads=191045158, day_uploads=479, total_users=5460144, day_users=251),
            Stats.from_dict(
                {"stats":
                    {"totalUploads": "191045158", "dayUploads": "479", "totalUsers": "5460144", "dayUsers": "251"}
                }
            )
        )


if __name__ == '__main__':
    unittest.main()
