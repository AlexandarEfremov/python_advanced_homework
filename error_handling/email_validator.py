email_input = input()

while email_input != "End":
    domain_names = ("com", "bg", "net", "org")

    class NameTooShortError(Exception):
        pass


    class MustContainAtSymbolError(Exception):
        pass


    class InvalidDomainError(Exception):
        pass


    if "@" not in email_input:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name, domain = email_input.split("@")

        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        domain_end = domain.split(".")[1]
        if domain_end not in domain_names:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    email_input = input()
