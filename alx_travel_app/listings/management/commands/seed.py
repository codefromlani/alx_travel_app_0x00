import random
from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        for _ in range(20):  
            Listing.objects.create(
                name=fake.company(),
                description=fake.text(max_nb_chars=200),
                price_per_night=random.randint(50, 500),
                location=fake.city()
            )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
