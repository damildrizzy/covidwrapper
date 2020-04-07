from covidwrapper import Covid

summary_keys = ['Countries', 'Global']
global_keys = ['NewConfirmed','TotalConfirmed', 'NewDeaths', 'TotalDeaths',
                'NewRecovered', 'TotalRecovered']
country_keys = global_keys.extend(["Country", "CountryCode", "Slug", "Date"])

def test_summary():
    response = Covid.summary()

    #response should be a dictionary object
    assert isinstance(response, dict)
    assert isinstance(response['Countries'], list)
    assert isinstance(response['Countries'][0], dict)
    assert set(summary_keys).issubset(response.keys())
    #assert set(global_keys).issubset(response['Global'].keys())
    #assert set(country_keys).issubset(response['Countries'][0].keys())

