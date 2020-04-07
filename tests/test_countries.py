from covidwrapper import Covid

country_keys = ['Country', 'Slug', 'ISO2']


def test_countries():
    response = Covid.countries()

    #response should be a dictionary object
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(country_keys).issubset(response[0].keys()) #all items in  country_keys must be included in the response