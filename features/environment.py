"""
(c) Copyright Jalasoft. 2023

environment.py
    file with all fixture methods for feature and step files
"""
import logging

import requests

from config.config import BASE_URL, HEADERS
from utils.logger import get_logger
from utils.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)


def before_all(context):
    """
    method to define variables that will be used in steps definitions
    :param context:   object     Context object to store and get variables
    """
    context.session = requests.Session()
    context.headers = HEADERS
    context.project_list = []
    context.section_list = []
    context.comment_list = []
    context.task_list = []
    context.url = BASE_URL
    LOGGER.debug("Headers before feature: %s", context.headers)
    projects = get_all_projects(context)
    LOGGER.debug(projects)
    context.project_id_from_all = projects["body"][1]["id"]


def before_feature(context, feature):
    context.feature_name = feature.name.lower()
    # context.url = BASE_URL + feature.name.lower()
    print("Before feature")


def before_scenario(context, scenario):
    LOGGER.debug("Scenario tags: %s", scenario.tags)
    LOGGER.debug("Scenario Name: %s", scenario.name)

    if "project_id" in scenario.tags:

        response = create_project(context=context, name_project="project x")
        context.project_id = response["body"]["id"]
        LOGGER.debug("Project id created: %s", context.project_id)
        context.project_list.append(context.project_id)

    if "section_id" in scenario.tags:

        response = create_section(context=context, project_id=context.project_id_from_all, section_name="section x")
        context.section_id = response["body"]["id"]
        LOGGER.debug("Section id created: %s", context.section_id)
        context.section_list.append(context.section_id)

    if "comment_id" in scenario.tags:

        response = create_comment(context=context, project_id=context.project_id_from_all, comment_name="comment x")
        context.comment_id = response["body"]["id"]
        LOGGER.debug("Comment id created: %s", context.comment_id)
        context.comment_list.append(context.comment_id)

    if "task_id" in scenario.tags:

        response = create_task(context=context,  task_content="task x")
        context.task_id = response["body"]["id"]
        LOGGER.debug("Task id created: %s", context.task_id)
        context.task_list.append(context.task_id)


def after_scenario(context, scenario):
    print("after scenario")


def after_feature(context, feature):
    print("After feature")


def after_all(context):
    print("After all")
    for project in context.project_list:
        url = f"{context.url}projects/{project}"
        RestClient().send_request(method_name="delete", session=context.session,
                                  url=url, headers=HEADERS)
        LOGGER.info("Deleting project: %s", project)
    for comment in context.comment_list:
        url = f"{context.url}comments/{comment}"
        RestClient().send_request(method_name="delete", session=context.session,
                                  url=url, headers=HEADERS)
        LOGGER.info("Deleting comment: %s", comment)
    for task in context.task_list:
        url = f"{context.url}tasks/{task}"
        RestClient().send_request(method_name="delete", session=context.session,
                                  url=url, headers=HEADERS)
        LOGGER.info("Deleting task: %s", task)


def create_project(context, name_project):

    body_project = {
        "name": name_project
    }
    response = RestClient().send_request(method_name="post", session=context.session,
                                         url=context.url+"projects", headers=context.headers,
                                         data=body_project)
    return response


def create_section(context, project_id, section_name):

    body_section = {
        "project_id": project_id,
        "name": section_name
    }
    response = RestClient().send_request(method_name="post", session=context.session,
                                         url=context.url+"sections", headers=context.headers,
                                         data=body_section)
    return response

def create_comment(context, project_id, comment_name):

    body_section = {
        "project_id": project_id,
        "content": comment_name
    }
    response = RestClient().send_request(method_name="post", session=context.session,
                                         url=context.url+"comments", headers=context.headers,
                                         data=body_section)
    return response

def create_task(context, task_content):

    body_section = {
        "content": task_content
    }
    response = RestClient().send_request(method_name="post", session=context.session,
                                         url=context.url+"tasks", headers=context.headers,
                                         data=body_section)
    return response


def get_all_projects(context):
    """
    Method to get all projects
    :param context:   object    Store contextual information about test
    :return:
    """
    response = RestClient().send_request(method_name="get", session=context.session,
                                         url=context.url + "projects", headers=context.headers)

    return response
