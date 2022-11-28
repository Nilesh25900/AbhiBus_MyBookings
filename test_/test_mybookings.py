from POM.bookingpage import Mybookings
import pytest
from Data import reading_mybooking

data_obj = reading_mybooking.read_data()
print(data_obj)

class Test_mybookingpage:

    @pytest.mark.parametrize("i", data_obj)
    def test_mybooking(self,_driver,i):
        mb = mb = Mybookings(_driver)
        mb.test_mybook1()
        mb.test_print(i)
        mb.test_mybook2()
        mb.test_cancel(i)








