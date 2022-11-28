import pytest
import time
from Data import reading_mybooking

booking_obj = reading_mybooking.read_locators()
print(booking_obj)

data_obj = reading_mybooking.read_data()
print(data_obj)


class Mybookings:

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj


    @pytest.mark.dependency()
    def test_mybook1(self):
        self.driver_obj.find_element(*booking_obj['click_mybookings']).click()
        time.sleep(2)
        self.driver_obj.find_element(*booking_obj['click_printBooking']).click()
        time.sleep(2)

    @pytest.mark.dependency(depends=["test_mybook1"])
    def test_print(self,i):
        self.driver_obj.find_element(*booking_obj["txt_bookingID"]).send_keys(i[0])
        time.sleep(2)
        self.driver_obj.find_element(*booking_obj["txt_mobileNo"]).send_keys(i[1])
        time.sleep(2)
        self.driver_obj.find_element(*booking_obj["click_retrive"]).click()
        self.driver_obj.back()


    @pytest.mark.dependency()
    def test_mybook2(self):
        self.driver_obj.find_element(*booking_obj["click_mybookings"]).click()
        time.sleep(2)
        self.driver_obj.find_element(*booking_obj["click_cancelBooking"]).click()
        time.sleep(2)

    @pytest.mark.dependency(depends=["test_mybook2"])
    def test_cancel(self,i):
        self.driver_obj.find_element(*booking_obj["txt_bookingID"]).send_keys(i[0])
        time.sleep(2)
        self.driver_obj.find_element(*booking_obj["txt_mobileNo"]).send_keys(i[1])
        time.sleep(2)
        self.driver_obj.find_element(*booking_obj["click_retrive"]).click()
