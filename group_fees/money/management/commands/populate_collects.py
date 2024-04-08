from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from money.models import Collect
from django.utils.crypto import get_random_string
import random

class Command(BaseCommand):
    help = 'Populate the Collect model with mock data'

    def handle(self, *args, **options):
        for i in range(1000):
            author = User.objects.order_by('?').first()
            name = get_random_string(length=10)
            occasion = random.choice([choice[0] for choice in Collect.Status.choices])
            description = get_random_string(length=50)
            target_amount = round(random.uniform(100, 1000), 2)
            collected_amount = round(random.uniform(0, target_amount), 2)
            contributors_count = random.randint(0, 100)
            cover_image = f'collect_covers/{random.randint(1, 10)}.jpg'
            completion_date = timezone.now()

            Collect.objects.create(
                author=author,
                name=name,
                occasion=occasion,
                description=description,
                target_amount=target_amount,
                collected_amount=collected_amount,
                contributors_count=contributors_count,
                cover_image=cover_image,
                completion_date=completion_date
            )

        self.stdout.write(self.style.SUCCESS('Successfully created mock data'))
