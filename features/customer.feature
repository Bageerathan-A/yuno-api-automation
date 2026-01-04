@customer @sanity
Feature: Customer API

  Scenario: Create customer with minimal fields
    Given valid customer headers
    When I create a customer
    Then the response status should be 201

  Scenario: Create customer with maximal fields
    Given valid customer headers
    When I create a customer with extra payload
      | name  | John Doe          |
      | email | john@example.com  |
      | phone | 9999999999        |
    Then the response status should be 201

  @regression
  Scenario: Create customer with invalid email
    Given valid customer headers
    When I create a customer with invalid email
    Then the response status should be 400

  @regression
  Scenario: Create customer with missing name
    Given valid customer headers
    When I create a customer without name
    Then the response status should be 400
