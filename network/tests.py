from django.test import TestCase
from .models import User, Status, Comment, Reaction

# Create your tests here.
class UserTestCase(TestCase):
    
    def setUp(self):
        # Create users
        user1 = User.objects.create(username='testuser', email='test@example.com', first_name='Test', last_name='User')
    
    def test_user_friends(self):
        x = User.objects.get(username='testuser')
        friends = x.friends.all()
        self.assertFalse(friends.filter(id=x.id).exists())

class CommentTestCase(TestCase):
    
    def setUp(self):
        # Create users
        user1 = User.objects.create(username='testuser1', email='test1@example.com', first_name='Test', last_name='User1')
        user2 = User.objects.create(username='testuser2', email='test2@example.com', first_name='Test', last_name='User2')

        # Create post
        post = Status.objects.create(user=user1, body='test post, please ignore')

        # Create comments
        com1 = Comment.objects.create(user=user2, commentPost=post, body='test comment 1')
        com2 = Comment.objects.create(user=user1, commentPost=post, body='test 2')
        com3 = Comment.objects.create(user=user2, commentPost=post, body='')

    def test_valid_comment(self):
        comment = Comment.objects.get(id=2)
        self.assertTrue(comment.is_valid_comment())
    
    def test_valid_comment_2(self):
        comment = Comment.objects.get(id=1)
        self.assertTrue(comment.is_valid_comment())
    
    def test_invalid_comment_body(self):
        comment = Comment.objects.get(id=3)
        self.assertTrue(comment.is_valid_comment())

class ReactionTestCase(TestCase):
    
    def setUp(self):
        # Create users
        user1 = User.objects.create(username='testuser1', email='test1@example.com', first_name='Test', last_name='User1')
        user2 = User.objects.create(username='testuser2', email='test2@example.com', first_name='Test', last_name='User2')
        user3 = User.objects.create(username='testuser3', email='test3@example.com', first_name='Test', last_name='User3')
        user4 = User.objects.create(username='testuser4', email='test4@example.com', first_name='Test', last_name='User4')
        user5 = User.objects.create(username='testuser5', email='test5@example.com', first_name='Test', last_name='User5')
        user6 = User.objects.create(username='testuser6', email='test6@example.com', first_name='Test', last_name='User6')

        # Create post
        post = Status.objects.create(user=user1, body='test post, please ignore')

        # Create reactions
        r1 = Reaction.objects.create(user=user1, reactPost=post, reaction='👍')
        r2 = Reaction.objects.create(user=user2, reactPost=post, reaction='🤪a')
        r3 = Reaction.objects.create(user=user3, reactPost=post, reaction='abc')
        r4 = Reaction.objects.create(user=user4, reactPost=post, reaction='ab')
        r5 = Reaction.objects.create(user=user5, reactPost=post, reaction='a')
        r6 = Reaction.objects.create(user=user6, reactPost=post, reaction='')

    def test_valid_react(self):
        user = User.objects.get(username='testuser1')
        reactions = Reaction.objects.get(user=user)
        self.assertTrue(reactions.is_valid_react())

    def test_invalid_emoji(self):
        user = User.objects.get(username='testuser2')
        reactions = Reaction.objects.get(user=user)
        self.assertTrue(reactions.is_valid_react())

    def test_invalid_length(self):
        user = User.objects.get(username='testuser3')
        reactions = Reaction.objects.get(user=user)
        self.assertTrue(reactions.is_valid_react())

    def test_invalid_chars(self):
        user = User.objects.get(username='testuser4')
        reactions = Reaction.objects.get(user=user)
        self.assertTrue(reactions.is_valid_react())

    def test_invalid_length_2(self):
        user = User.objects.get(username='testuser5')
        reactions = Reaction.objects.get(user=user)
        self.assertTrue(reactions.is_valid_react())

    def test_invalid_str(self):
        user = User.objects.get(username='testuser6')
        reactions = Reaction.objects.get(user=user)
        self.assertTrue(reactions.is_valid_react())