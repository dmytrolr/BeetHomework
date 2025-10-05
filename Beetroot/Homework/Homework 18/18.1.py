class Validate:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        if not isinstance(self.email, str):
            raise TypeError("Email must be a string.")

        if "@" not in self.email:
            raise ValueError("Email must contain '@'.")

        parts = self.email.split("@")
        if len(parts) != 2:
            raise ValueError("Email must contain only one '@'.")

        local, domain = parts

        if "." not in domain:
            raise ValueError("Domain part must contain '.' for domain zone marking.")

        # prefix verify
        if not local:
            raise ValueError("Email prefix must not be empty.")
        if local[0] in "._-":
            raise ValueError("Prefix must not start with '.', '_' or '-'.")
        if ".." in local or "__" in local or "--" in local:
            raise ValueError("Prefix must not contain consecutive special characters.")

        for i, ch in enumerate(local):
            if ch in "._-":
                if i == len(local) - 1 or not local[i + 1].isalnum():
                    raise ValueError("Special characters must be followed by a letter or number.")

        # domain verify
        domain_parts = domain.split(".")
        if len(domain_parts[-1]) < 2:
            raise ValueError("Domain zone must be at least two characters.")
        for part in domain_parts:
            if not part:
                raise ValueError("Domain must not contain empty parts")
            if not all(c.isalnum() or c == "-" for c in part):
                raise ValueError("Domain parts must contain only letters, numbers or '-'.")


test_emails = [
    "abc-d@mail.com",
    "abc.def@mail.cc",
    "abc_def@mail.com",
    "abc-@mail.com",
    ".abc@mail.com",
    "abc..def@mail.com",
    "abc.def@mail.c",
    "abc.def@mail#archive.com",
    "abc.def@mail"
]

for email in test_emails:
    try:
        obj = Validate(email)
        print(f"{email} is valid. ")
    except Exception as e:
        print(f"{email} is invalid — {e}.")
