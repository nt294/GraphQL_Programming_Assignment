from django.shortcuts import render
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def main_page(request):
    transport = RequestsHTTPTransport(url="https://countries.trevorblades.com/")
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Form the query in the GraphQL language
    query = gql(
        """
        {
           countries {
              name
              code      
           }
        }
        """
    )

    result_dictionary = client.execute(query)
    retrieved_countries = result_dictionary.get('countries')

    countries = []
    country_codes_dict = {}

    # Extract information from each dictionary
    for dictionary in retrieved_countries:
        countries.append(dictionary.get("name"))
        country_codes_dict[dictionary.get("name")] = dictionary.get("code")

    # Returns a list of countries and a country:code dictionary in the context
    return render(request, "index.html", {"countries": sorted(countries), "country_codes": country_codes_dict})
