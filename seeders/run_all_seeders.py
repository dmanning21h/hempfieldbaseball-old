import os

seeders = [
    'lift_type_seeder.py',
    'velocity_type_seeder.py',
    'time_type_seeder.py',
    'distance_type_seeder.py',
    'sets_seeder.py',
    'strength_increments_seeder.py',
    'position_seeder.py',
    'coach_role_seeder.py',
    'height_seeder.py',
    'book_type_seeder.py',
    'link_type_seeder.py',
    'document_type_seeder.py',
]

for seeder in seeders:
    os.system(f'python {seeder}')
