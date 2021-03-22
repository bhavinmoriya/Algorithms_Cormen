class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self,first,last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay
        Employee.num_of_emps += 1
    def fullname(self):
      return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
      self.pay = self.pay * self.raise_amt
    @classmethod
    def set_raise_amt(cls, amt):
      cls.raise_amt = amt

print(Employee.num_of_emps)      
emp1 = Employee('Bhavin', 'Moriya',20000)
emp2 = Employee('Lais','Moreira','30000')
emp1.apply_raise()
emp1.set_raise_amt(1.05)
print(Employee.num_of_emps)      

Employee.__dict__
