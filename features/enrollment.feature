@enrollment @sanity
Feature: Enrollment API

  Scenario: Enroll card for valid customer
    Given valid enrollment headers
    When I enroll a card for a customer
    Then the response status should be 201

  Scenario: Enroll card with maximal fields
    Given valid enrollment headers
    When I enroll a card with extra payload
      | card_number   | 4111111111111111 |
      | expiry_month  | 12               |
      | expiry_year   | 2028             |
      | cvv           | 123              |
      | customer_id   | cust_001         |
    Then the response status should be 201

  @regression
  Scenario: Enroll card with invalid customer_id
    Given valid enrollment headers
    When I enroll a card for invalid customer_id
    Then the response status should be 400

  @regression
  Scenario: Enroll card with expired card
    Given valid enrollment headers
    When I enroll a card with expired card
    Then the response status should be 400
