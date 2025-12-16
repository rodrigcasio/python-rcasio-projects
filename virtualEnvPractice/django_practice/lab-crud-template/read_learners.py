# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings')
from django.db import connection

# Ensures settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date

# find students with last name "Smith"
smith_learner = Learner.objects.filter(last_name='Smith')
print(f"1. Find learner with last name 'Smith': {smith_learner}")
print('\n')

# Order by bod descending, and select the first dob two objects
learners = Learner.objects.order_by('-dob')[0:2]
print(f"2. Find top two yongest learners: {learners}")

"""
OUTPUT:
"""

