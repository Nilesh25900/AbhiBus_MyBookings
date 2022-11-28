Feature: MyBookings


  Background: common steps
    Given launch the browser
    When open abhibus homepage
    And click on my bookings


  Scenario: click on print bookings
    And click on print booking
    Then verify print booking page is visible or not


  Scenario:  entering the booking details for print booking
    And click on print booking
    And enter bookig id
    And enter mobile no
    And click on "retrive" button
    Then verify that booking details are visible or not


  Scenario: click on cancel bookings
    And click on cancel booking
    Then verify cancel booking page is visible or not


  Scenario:  entering the booking details for cancel booking
    And click on cancel booking
    And enter bookig id
    And enter mobile no
    And click on "retrive" button
    Then verify that cancelation is visible or not
























