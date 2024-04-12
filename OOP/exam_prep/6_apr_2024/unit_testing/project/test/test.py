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

    def test_a_post_creation_if_in_list(self):
        self.playa.create_post("marketing")
        self.assertEqual([{'content': 'marketing', 'likes': 0, 'comments': []}], self.playa._posts)

    def test_actual_post_creation(self):
        expect = "New anime post created by Alex on Instagram."
        self.assertEqual(expect, self.playa.create_post("marketing"))

    def test_post_like_with_invalid_index(self):
        self.playa.create_post("marketing")
        self.assertEqual("Invalid post index.", self.playa.like_post(3))

    def test_post_like_with_max_amount_of_likes(self):
        self.playa.create_post("marketing")
        self.playa._posts[0]["likes"] = 10
        self.assertEqual("Post has reached the maximum number of likes.", self.playa.like_post(0))

    def test_normal_post_like(self):
        self.playa.create_post("marketing")
        self.playa.like_post(0)
        self.assertEqual("Post liked by Alex.", self.playa.like_post(0))

    def test_if_after_like_post_likes_increase_by_one(self):
        self.playa.create_post("marketing")
        self.playa._posts[0]["likes"] = 8
        self.playa.like_post(0)
        self.assertEqual(9, self.playa._posts[0]["likes"])

    def test_comment_on_post_with_less_than_10_len(self):
        self.playa.create_post("marketing")
        ex = "Comment should be more than 10 characters."
        self.assertEqual(ex, self.playa.comment_on_post(0, "abc"))

    def test_if_can_find_comment_in_list(self):
        self.playa.create_post("marketing")
        self.playa.comment_on_post(0, "Amazing content")
        ex = [{'content': "marketing", 'likes': 0, 'comments': [{'user': 'Alex', 'comment': 'Amazing content'}]}]
        self.assertEqual(ex, self.playa._posts)

    def test_adding_the_comment_expect_message(self):
        self.playa.create_post("marketing")
        result = self.playa.comment_on_post(0, "Amazing content")

        self.assertEqual("Comment added by Alex on the post.", result)


if __name__ == "__main__":
    main()