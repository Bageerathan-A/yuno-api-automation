@refund @sanity
Feature: Refund Payment API

  Scenario: Refund with valid minimal fields
    Given valid refund headers
    When I create a refund
    Then the response status should be 201

  Scenario: Refund with maximal fields
    Given valid refund headers
    When I create a refund with extra payload
      | reason      | Customer requested refund |
      | note        | Test refund edge case    |
    Then the response status should be 201

  @regression
  Scenario: Refund amount greater than payment
    Given valid refund headers
    When I create a refund with excessive amount
    Then the response status should be 400

  @regression
  Scenario: Refund with invalid payment_id
    Given valid refund headers
    When I create a refund with invalid payment id
    Then the response status should be 400
