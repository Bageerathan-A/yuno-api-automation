@purchase @sanity
Feature: Purchase Payment API

  Scenario: Create purchase with minimal fields
    Given valid purchase headers
    When I create a purchase
    Then the response status should be 201

  Scenario: Create purchase with maximal fields
    Given valid purchase headers
    When I create a purchase with extra payload
      | customer_payer.id    | cust_001        |
      | customer_payer.email | test@customer.com |
      | additional_data.note | Test purchase   |
    Then the response status should be 201

  @regression
  Scenario: Purchase with invalid card number
    Given valid purchase headers
    When I create a purchase with invalid card
    Then the response status should be 400

  @regression
  Scenario: Purchase without account_id
    Given valid purchase headers
    When I create a purchase with missing account id
    Then the response status should be 400
