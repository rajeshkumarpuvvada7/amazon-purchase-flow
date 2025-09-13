Feature: Amazon Homepage functionality
  As an Amazon customer
  I want to search for a product and add it to the cart
  So that I can validate the cart after deleting the item

  Scenario: Search and add an iPhone to the cart, then delete and validate
    Given I am on the Amazon homepage
    When I search for "Iphone"
    And Click Search button
    And Add phone to cart
    And Go to cart
    And click delete hyperlink for mobile
    Then validate text after delete mobile