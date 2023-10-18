@tasks @acceptance

Feature: Tasks

  @project_id
  Scenario:  Verify POST section creates the task correctly with project id
      As a user I want to create a task from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "POST" method using the "task data" as parameter
    """
    {
       "content": "task created with project id 2",
       "project_id": "project_id"
    }
    """
    Then I receive a 200 status code in response

  Scenario:  Verify POST section creates the task correctly
      As a user I want to create a task from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "POST" method using the "task data" as parameter
    """
    {
      "content": "task created"
    }
    """
    Then I receive a 200 status code in response

  @task_id
  Scenario: Verify POST project endpoint updates a comment with the content provided

    Given I set the base url and headers
    When I call to taks endpoint using "POST" method using the "update task data" as parameter
    """
    {
      "content": "task updated"
    }
    """
    Then I receive a 200 status code in response

  @task_id
  Scenario:  Verify GET one task is returning all data correctly
      As a user I want to GET the task from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "GET" method using the "task_id" as parameter
    Then I receive a 200 status code in response
    And I validate the response data

  @task_id
  Scenario:  Verify DELETE task delete the section correctly
      As a user I want to delete a task from TODOIST API

    Given I set the base url and headers
    When I call to tasks endpoint using "DELETE" method using the "task_id" as parameter