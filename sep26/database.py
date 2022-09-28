class Patient:

    def __init__(self, first_name, last_name, id, age):
        self.first_name = first_name
        self.last_name = last_name
        self.patient_id = id
        self.age = age
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(patient_first_name, patient_last_name, patient_id, patient_age):
    new_patient = Patient()
    new_patient.first_name = patient_first_name
    new_patient.last_name = patient_last_name
    new_patient.patient_id = patient_id
    new_patient.age = patient_age
    return new_patient


def print_database(db):
    for patient_id in db.keys():
        current_patient = db[patient_id]
        print(current_patient)
        print("Name: {}, id: {}, age: {}".format(
            current_patient["First Name"], current_patient["Id"], current_patient["Age"]))


def find_patient(db, id_no):
    patient = db[id_no]
    return False


def add_test_to_patient(db, id_no, test_name, test_value):
    patient = db[id_no]
    patient["Tests"].append((test_name, test_value))


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


def get_full_name(patient):
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name


def main():
    x = Patient("Suryansh", "Jain", "", "")
    x.first_name = "Suryansh"
    x.last_name = "Jain"
    print(x.full_name())
    print(type(x))
    exit()

    db = {}
    db[11] = create_patient_entry("Ann", "Ables", 11, 30)
    db[22] = create_patient_entry("Bob", "Boyles", 22, 34)
    db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    print_database(db)
    add_test_to_patient(db, 3, "HDL", 100)
    print_database(db)
    print("Patient {} is a {}".format(get_full_name(
        db[3]), adult_or_minor(db[3])))


if __name__ == '__main__':
    main()
