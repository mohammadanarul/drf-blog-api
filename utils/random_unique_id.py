import uuid


def random_generate_bank_account_num():
    return str(uuid.uuid4()).replace('-', '').upper()[:20]


print(random_generate_bank_account_num())
