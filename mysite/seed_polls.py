import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django  # noqa: E402

django.setup()

from django.utils import timezone  # noqa: E402
from polls.models import Choice, Question  # noqa: E402

samples = [
    {
        "question_text": "What is your favorite movie genre?",
        "choices": ["Action", "Comedy", "Drama", "Sci-Fi"],
    },
    {
        "question_text": "Which city would you like to visit next?",
        "choices": ["Tokyo", "Paris", "New York", "Rome"],
    },
]

for item in samples:
    q, created = Question.objects.get_or_create(
        question_text=item["question_text"],
        defaults={"pub_date": timezone.now()},
    )
    for c in item["choices"]:
        Choice.objects.get_or_create(question=q, choice_text=c, defaults={"votes": 0})

print("Sample polls seeded (if missing).")
