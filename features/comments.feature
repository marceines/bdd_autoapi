@comments @acceptance

Feature: Comments



  @project_id
  Scenario:  Verify POST section creates the comment correctly
      As a user I want to create a comment from TODOIST API

    Given I set the base url and headers
    When I call to comments endpoint using "POST" method using the "comment data" as parameter
    """
    {
      "project_id": "project_id",
      "content": "Comment created"
    }
    """
    Then I receive a 200 status code in response

  @comment_id
  Scenario: Verify POST project endpoint updates a comment with the content provided

    Given I set the base url and headers
    When I call to comments endpoint using "POST" method using the "update comment data" as parameter
    """
    {
      "content": "Comment updated"
    }
    """
    Then I receive a 200 status code in response

  @comment_id
  Scenario:  Verify GET one comment is returning all data correctly
      As a user I want to GET the comment from TODOIST API

    Given I set the base url and headers
    When I call to comments endpoint using "GET" method using the "comment_id" as parameter
    Then I receive a 200 status code in response
    And I validate the response data

  @comment_id
  Scenario:  Verify DELETE comment delete the section correctly
      As a user I want to delete a task from TODOIST API

    Given I set the base url and headers
    When I call to comments endpoint using "DELETE" method using the "comment_id" as parameter

