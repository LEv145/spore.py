from datetime import datetime
import unittest

from spore_api.enums import AssetType
from spore_api.models import (
    Stats,
    Creature,
    User,
    Sporecast,
    Asset,
    Achievement,
    Comment,
    Buddy
)


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

    def test_creature(self):
        self.assertEqual(
            Creature(
                cost=4065,
                health=3,
                height=1.3428643,
                meanness=9,
                cuteness=71.26385,
                sense=1,
                bonecount=44,
                footcount=4,
                graspercount=0,
                basegear=0,
                carnivore=1,
                herbivore=0,
                glide=0,
                sprint=2,
                stealth=2,
                bite=3,
                charge=2,
                strike=4,
                spit=0,
                sing=1,
                dance=2,
                gesture=5,
                posture=0,
            ),
            Creature.from_dict({'creature': {
                    'status': 1,
                    'input': 500267423060,
                    'cost': 4065,
                    'health': 3,
                    'height': 1.3428643,
                    'meanness': 9,
                    'cuteness': 71.26385,
                    'sense': 1,
                    'bonecount': 44,
                    'footcount': 4,
                    'graspercount': 0,
                    'basegear': 0,
                    'carnivore': 1,
                    'herbivore': 0,
                    'glide': 0,
                    'sprint': 2,
                    'stealth': 2,
                    'bite': 3,
                    'charge': 2,
                    'strike': 4,
                    'spit': 0,
                    'sing': 1,
                    'dance': 2,
                    'gesture': 5,
                    'posture': 0
                }
            })
        )

    def test_user(self):
        self.assertEqual(
            User(
                id=2262746427,
                image_url="http://www.spore.com/static/avatar/226/274/642/howlsHouse-1.gif",
                tagline="make juicy things!",
                create_at=datetime(2008, 6, 9, 20, 32)
            ),
            User.from_dict({'user': {
                    'status': 1,
                    'input': 'MaxisDangerousYams',
                    'id': 2262746427,
                    'image': 'http://www.spore.com/static/avatar/226/274/642/howlsHouse-1.gif',
                    'tagline': 'make juicy things!',
                    'creation': '2008-06-09 20:32:00.0'
                }
            })
        )

    def test_sporecast(self):
        self.assertEqual(
            Sporecast(
                title="Aaarrrggg's Top Picks",
                subtitle="My favourite finds on the Sporepedia, enjoy! ^_^",
                id=500175165202,
                author_name="Aaarrrggg",
                update_at=datetime(2008, 12, 10, 17, 16, 57, 361000),
                rating=116,
                subscription_count=862,
                tags=[],
                assets_count=924
            ),
            Sporecast.from_dict({'sporecast': {
                'title': "Aaarrrggg's Top Picks",
                'subtitle':
                'My favourite finds on the Sporepedia, enjoy! ^_^',
                'id': "500175165202",
                'author':
                'Aaarrrggg',
                'updated': '2008-12-10 17:16:57.361',
                'rating': "116",
                'subscriptioncount': "862",
                'tags': '[]',
                'count': 924
                }
            })
        )

        self.assertEqual(
            Sporecast(
                title="Aaarrrggg's Top Picks",
                subtitle="My favourite finds on the Sporepedia, enjoy! ^_^",
                id=500175165202,
                author_name="Aaarrrggg",
                update_at=datetime(2008, 12, 10, 17, 16, 57, 361000),
                rating=116,
                subscription_count=862,
                tags=['mecha', 'black ops', 'mechs', 'didzo', '7 deadly sins', 'rapture'],
                assets_count=924
            ),
            Sporecast.from_dict({'sporecast': {
                'title': "Aaarrrggg's Top Picks",
                'subtitle':
                'My favourite finds on the Sporepedia, enjoy! ^_^',
                'id': "500175165202",
                'author':
                'Aaarrrggg',
                'updated': '2008-12-10 17:16:57.361',
                'rating': "116",
                'subscriptioncount': "862",
                'tags': '[mecha, black ops, mechs, didzo, 7 deadly sins, rapture]',
                'count': 924
                }
            })
        )

    # def test_asset(self):
    #     self.assertEqual(
    #         Asset(
    #             name="Snorkoluf",
    #             author_name="MaxisMichael",
    #             author_id=2251081551,
    #             create_at=datetime(2008, 7, 12, 8, 1, 36, 119000),
    #             description="This guy's nose walks around. He just follows",
    #             tags=["zipcode 94107"],
    #             type=AssetType.creature,
    #             subtype="0x9ea3031a",
    #             rating=0.46511626,
    #             parent=None
    #         ),
    #         Asset.from_dict(

    #         )
    #     )

if __name__ == '__main__':
    unittest.main()
