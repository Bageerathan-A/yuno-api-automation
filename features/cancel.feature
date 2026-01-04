@cancel @sanity
Feature: Cancel Payment API

  Scenario: Cancel authorized payment successfully
    Given valid cancel headers
    When I cancel the payment
    Then the response status should be 201

  @regression
  Scenario: Cancel payment with invalid payment_id
    Given valid cancel headers
    When I cancel payment with invalid payment_id
    Then the response status should be 400

  @regression
  Scenario: Cancel payment that is already captured
    Given valid cancel headers
    When I cancel a captured payment
    Then the response status should be 400
