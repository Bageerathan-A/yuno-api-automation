@verify @sanity
Feature: Verify Payment API

  Scenario: Verify a valid payment
    Given valid verify headers
    When I verify the payment
    Then the response status should be 200

  @regression
  Scenario: Verify with invalid payment_id
    Given valid verify headers
    When I verify payment with invalid payment_id
    Then the response status should be 400

  @regression
  Scenario: Verify payment not yet created
    Given valid verify headers
    When I verify payment that does not exist
    Then the response status should be 404
