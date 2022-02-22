from unittest import TestCase

import requests.exceptions
from django.test import Client
from gql import gql, Client as gqlClient
from gql.transport.requests import RequestsHTTPTransport


class YourTestClass(TestCase):
    client = Client(HTTP_USER_AGENT='Mozilla/5.0')

    def test_view_context(self):
        """
        Tests that the main_page view returns a response with correct context items
        """

        # Sends a GET request to the applications root URL to trigger the main_page view
        response = self.client.get('/')

        valid_context = False
        try:
            country_list = response.context['countries']
            country_codes = response.context['country_codes']
            valid_context = True
        # Key error if both context dictionaries are not present
        except KeyError:
            pass

        # Assert that the context dictionaries are present
        self.assertTrue(valid_context)


    def test_graphql_query(self):
        """
        Tests that a query can be sent to the API, and that the expected type is returned
        """

        transport = RequestsHTTPTransport(url="https://countries.trevorblades.com/")
        graphql_client = gqlClient(transport=transport, fetch_schema_from_transport=True)

        query = gql(
            """
            {
                country(code: "GB") {
                    name     
                }
            }
            """
        )

        try:
            result = graphql_client.execute(query)
        except requests.exceptions.ConnectionError:
            # Fail if unable to connect to the API
            self.fail("Could not connect to API")

        # Checks that the object returned is of type dict
        self.assertTrue(isinstance(result, dict))