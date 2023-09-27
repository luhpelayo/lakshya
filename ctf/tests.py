from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Questions, Submission

class YourAppTestCase(TestCase):
    def setUp(self):
        # Configura datos iniciales para tus pruebas
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = UserProfile.objects.create(user=self.user, Rid='EINC-5e5a', score=0, totlesub=0, latest_sub_time='00:00')

        self.question = Questions.objects.create(Qid=1, Qtitle='Test Question', Qdes='Test Description', level='E', Easy=1, Med=0, Hard=0, flag='pict_CTF{}', points=100, solved_by=0, category='category_web')

    def test_user_profile_str(self):
        # Prueba el método __str__ del modelo UserProfile
        self.assertEqual(str(self.profile), 'testuser')

    def test_question_creation(self):
        # Prueba la creación de una pregunta
        self.assertEqual(self.question.Qid, 1)
        self.assertEqual(self.question.Qtitle, 'Test Question')
        # Agrega más aserciones aquí según tus necesidades

    def test_submission_creation(self):
        # Prueba la creación de una presentación (submission)
        submission = Submission.objects.create(question=self.question, user=self.profile, curr_score=100, solved=1, sub_time='01:00')
        self.assertEqual(submission.curr_score, 100)
        self.assertEqual(submission.solved, 1)
        # Agrega más aserciones aquí según tus necesidades

    def test_question_category_choices(self):
        # Prueba que las opciones de categoría en el modelo Questions son válidas
        valid_categories = [choice[0] for choice in Questions._meta.get_field('category').choices]
        self.assertIn('category_web', valid_categories)
        self.assertIn('category_reversing', valid_categories)
        # Agrega más aserciones aquí según tus necesidades

    # Agrega más pruebas según tus necesidades

