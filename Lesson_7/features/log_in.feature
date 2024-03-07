# Created by alberthembd at 3/7/24
Feature: log into Target account
  # Enter feature description here
  #
Scenario:
  Given Open target.com
  When Click Sign In
  And From side navigation, click sign in
  And Input email and password on SignIn page
  And Click Sign In
  Then Verify user is logged in (sign in form should disappear)