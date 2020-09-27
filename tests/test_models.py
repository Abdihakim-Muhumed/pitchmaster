import unittest
from app.models import User, Pitch, Comment

class TestUser(unittest.TestCase):
    '''class to test behaviour of User Model'''
    def setUp(self):
        self.new_user = User(password = 'Abdi9999')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_accessing_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('Abdi999'))
class TestPitch(unittest.TestCase):
    '''Test class to test behaviour of Pitch Model'''
    def setUp(self):
        self.new_pitch = Pitch(pitch_id = 1,title = 'The title',content='The content',category = 'pickuplines',user_id = 1)
    def test_save_pitch(self):
        pitch1 = Pitch(pitch_id = 2,title = 'The title',content='The content',category = 'pickuplines',user_id = 1)
        pitch1.save_pitch()
        self.assertEqual(pitch1.pitch_id,2)
    def test_get_pitch(self):
        pitch2 = Pitch(pitch_id = 3,title = 'The title',content='The content',category = 'pickuplines',user_id = 1)
        got_pitch = Pitch.get_pitch(3)
        self.assertEqual(got_pitch.pitch_id,3)
    def test_get_pitchs(self):
        pitch3= Pitch(pitch_id = 1,title = 'The title',content='The content',category = 'pickuplines',user_id = 1)
        pitches = Pitch.get_pitches('pickuplines')
        self.assertEqual(len(pitches),1)
    def test_get_all_pitches(self):
        pitch4 = Pitch(pitch_id = 1,title = 'The title',content='The content',category = 'pickuplines',user_id = 1)
        pitches = Pitch.get_all_pitches()
        self.assertEqual(len(pitches),1)
class TestComment(unittest.TestCase):
    '''test class to test behaviour of Comment Model'''
    def setUp():
        self.new_comment = Comment(id = 1,comment = 'Good one',user_id=1,pitch_id=1)
    def test_save_comment(self):
        comment1 = Comment(id = 2,comment = 'Good one',user_id=1,pitch_id=1)
        comment1.save_comment()
        self.assertEqual(comment1.id,1)
    def test_get_comments(self):
        comment2 = Comment(id = 3,comment = 'Good one',user_id=1,pitch_id=1)
        comment3 = Comment(id = 4,comment = 'Good one',user_id=1,pitch_id=1)
        comment2.save_comment()
        comment3.save_comment()
        comments = Comment.get_comments()
        self.assertGreater(len(comments),1)