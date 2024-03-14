import os
import sys

# Add the 'generated' directory to the Python path
sys.path.append(os.path.abspath('./generated'))

import person_pb2


def main():

    body_map = {
        "height": "6 feet",
        "weight": "180 pounds"
    }

    # Create a Car instance
    car = person_pb2.Person.Car(
        brand="Toyota",
        model="Camry"
    )

    # Create a Person instance
    person = person_pb2.Person(
        name="John Doe",
        email="john.doe@example.com",
        id=12345,
        salary=50000.00,
        employed=True,
        gender=person_pb2.Person.MALE,
        random=b'\x01\x02\x03\x04',
        body_map=body_map,
        money=[100, 500, 1000],
        person_car=car,
    )

    # Setting up the payment method
    person.myPayment.credit_card.card_number = "1234567890123456"
    person.myPayment.credit_card.cardholder_name = "John Doe"
    person.myPayment.credit_card.expiry_date = "12/25"
    person.myPayment.credit_card.cvv = "123"

    ################################################

    # Serialize the Person to a binary string
    serialized_person = person.SerializeToString()

    # Deserialize the binary string back into a new Person object
    new_person = person_pb2.Person()
    new_person.ParseFromString(serialized_person)

    # Print the deserialized Person
    print("Deserialized Person:", new_person)

    ################################################

    # Save serialized data to a file
    with open("person.bin", "wb") as f:
        f.write(serialized_person)

    # Read serialized data from the file
    with open("person.bin", "rb") as f:
        serialized_person = f.read()

    # Deserialize the binary string back into a new Person object
    new_person = person_pb2.Person()
    new_person.ParseFromString(serialized_person)

    # Print the deserialized Person
    print("Deserialized Person:\n", new_person)


if __name__ == "__main__":

    main()
