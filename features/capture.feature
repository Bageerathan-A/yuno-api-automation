@capture @sanity
Feature: Capture Payment API

  Scenario: Capture authorized payment successfully
    Given valid capture headers
    When I capture the payment
    Then the response status should be 201

  @regression
  Scenario: Capture with invalid payment_id
    Given valid capture headers
    When I capture payment with invalid payment_id
    Then the response status should be 400

  @regression
  Scenario: Capture without prior authorization
    Given valid capture headers
    When I capture payment without authorization
    Then the response status should be 400
