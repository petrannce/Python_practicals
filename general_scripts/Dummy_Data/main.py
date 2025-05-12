from faker import Faker

fake = Faker()

print("Generating dummy data...")
def generate_dummy_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "date_of_birth": fake.date_of_birth(),
        }
        data.append(record)
    return data

num_records = int(input("Enter the number of records to generate: "))
dummy_data = generate_dummy_data(num_records)

print("Generated dummy data:")
for record in dummy_data:
    print(record)