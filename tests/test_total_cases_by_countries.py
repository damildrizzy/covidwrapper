from covidwrapper import Covid

def test_total_cases():
    country_instance = Covid('nigeria', 'deaths')
    response = country_instance.total_cases_by_country()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'Nigeria'

def test_total_cases_since_day1():
    country_instance = Covid('ghana', 'recovered')
    response = country_instance.total_cases_since_day1()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'Ghana'
