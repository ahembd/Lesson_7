# Created by alberthembd at 2/8/24
Feature: # create_new_amazon_account
  # automated process for creating a new amazon account

  Scenario: # create new amazon account
    # Enter steps here
  Given that the user has navigated to the Create a new Amazon account webpage
    And The user already has a valid user name with which to open his new account.
    When the user enters his valid user name and a new valid password
    And he/she clicks the Submit button
    Then a new account is created.