class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}."

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set."
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, str):
        namestr = str.split("@")[0]
        names = namestr.split(".")
        self.fname = names[0]
        self.lname = names[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


debjit = Employee("Debijt", "Pramanick")
rohan = Employee("Rohan", "Das")


print(debjit.email)
debjit.email = 'sujan.pramanick@gmail.com'
print(debjit.email, debjit.fname)

del debjit.email
print(debjit.email)