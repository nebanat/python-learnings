import pytest

from dummy.employee import Employee

NAME: str = 'Arjan'
EMPLOYEE_ID: int = 12345

@pytest.fixture()
def employee():
    print("setting up")
    return Employee(name=NAME, employee_id=EMPLOYEE_ID)

class TestEmployeeComputePayouts:
    def test_employee_payout_returns_a_float(self, employee):
        """Whether payout returns a float"""
        assert isinstance(employee.compute_payout(), float)
    
    def test_employee_payout_no_commission_no_hours(self, employee):
        """Whether payout returns a float"""
        assert employee.compute_payout() == pytest.approx(1000.0)
    
    def test_employee_payout_no_commission(self, employee):
        """Whether payout returns a float"""
        employee.hours_worked = 10.0
        assert employee.compute_payout() == pytest.approx(2000.0)
    
    def test_employee_payout_with_commission(self, employee):
        """Whether payout is correctly computed in case 
        of 10 contracts landed and 10 hours worked"""
        employee.hours_worked = 10.0
        employee.contracts_landed = 10
        assert employee.compute_payout() == pytest.approx(3000.0)
    
    def test_employee_payout_with_commission_disabled(self, employee):
        """Whether payout is correctly computed in case 
        of 10 contracts landed and 10 hours worked"""
        employee.hours_worked = 10.0
        employee.contracts_landed = 10
        employee.has_commission = False
        assert employee.compute_payout() == pytest.approx(2000.0)