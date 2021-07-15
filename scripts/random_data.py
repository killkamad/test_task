from collections import defaultdict
import random
from mainapp.models import Record, Status, UserProfile

from faker import Faker

fake = Faker()
fake_data = defaultdict(list)
for _ in range(1000):
    fake_data["phone"].append(fake.phone_number())
    fake_data["text"].append(fake.paragraph(nb_sentences=1))
    fake_data["status_id"].append(random.randint(1, 2))
    fake_data["user_id"].append(random.randint(1, 2))

print(len(fake_data['phone']))
for i in range(1000):
    user = UserProfile.objects.get(user=fake_data['user_id'][i])
    status = Status.objects.get(id=fake_data['status_id'][i])
    rec = Record.objects.create(phone=fake_data['phone'][i],
                                description=fake_data['text'][i],
                                status_id=status,
                                user_id=user)