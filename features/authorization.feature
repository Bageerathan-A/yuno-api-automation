@authorization @sanity
Feature: Authorization Payment API

  Scenario: Authorize payment with minimal fields
    Given valid authorization headers
    When I authorize a payment
    Then the response status should be 201

  Scenario: Authorize payment with maximal fields
    Given valid authorization headers
    When I authorize a payment with extra payload
      | customer_payer.id    | cust_001        |
      | customer_payer.email | test@customer.com |
      | additional_data.note | Test authorization |
    Then the response status should be 201

  @regression
  Scenario: Authorization with zero amount
    Given valid authorization headers
    When I authorize payment with amount zero
    Then the response status should be 400

  @regression
  Scenario: Authorization with invalid card
    Given valid authorization headers
    When I authorize payment with invalid card
    Then the response status should be 400
