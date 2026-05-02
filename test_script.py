import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feedback_system.settings')
django.setup()
from feedback.models import Feedback

# Add some fake feedbacks
Feedback.objects.create(category='Faculty', target='Prof. Smith', message='Great teaching style and very approachable.', rating=5)
Feedback.objects.create(category='Subject', target='Data Structures', message='The syllabus is very dense and hard to follow at times.', rating=3)
Feedback.objects.create(category='Infrastructure', target='Library', message='The AC on the 2nd floor does not work.', rating=2)

try:
    f = Feedback(category='Faculty', target='Prof. Doe', message='This class is stupid.', rating=1)
    f.full_clean()
    print('Failed: Bad word was not caught.')
except Exception as e:
    print('Success: Bad word filter worked!', e)

print('Total feedbacks in DB:', Feedback.objects.count())
