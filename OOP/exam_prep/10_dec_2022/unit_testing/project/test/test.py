from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    allowed_platforms = ['Instagram', 'YouTube', 'Twitter']

    def setUp(self):
        self.playa = SocialMedia("Alex", "Instagram", 100, "anime")

    def test_correct_init(self):
        self.assertEqual("Alex", self.playa._username)
        self.assertEqual("Instagram", self.playa._platform)
        self.assertEqual(100, self.playa._followers)
        self.assertEqual("anime", self.playa._content_type)
        self.assertEqual([], self.playa._posts)

    def test_validate_platform_expect_fail(self):
        with self.assertRaises(Exception) as ex:
            self.playa.platform = "Facebook"
        self.assertEqual(f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ex.exception))

    def test_followers_expect_negative(self):
        with self.assertRaises(Exception) as ex:
            self.playa.followers = -1
        self.assertEqual("Followers cannot be negative.", str(ex.exception))

    def test_a_post_creation(self):
        res = self.playa.create_post("get ready")
        new_post = {'content': "get ready", 'likes': 0, 'comments': []}
        ex_res = "New get ready created by Alex on Instagram"
        self.assertEqual(new_post, self.playa._posts)
        self.assertEqual(res, ex_res)

if __name__ == "__main__":
    main()