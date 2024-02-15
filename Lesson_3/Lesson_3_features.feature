# Created by alberthembd at 2/14/24
Feature: # Test scenarios for CSS test scripts
  # Enter feature description here

  Scenario: # Create New Amazon account
    Given user is the on the Amazon Create a New Account
    And user has a valid user name and password
    When user enters a valid user name into the Create a New Account page
    And enters a valid password
    And presses "continue"
    Then a new user account is created