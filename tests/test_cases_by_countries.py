from covidwrapper import Covid

def test_cases_by_countries():
    country_instance = Covid('barbados')
    response = country_instance.cases_by_country()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'Barbados'

def test_with_status_deaths():
    country_instance = Covid('barbados', 'deaths')
    response = country_instance.cases_by_country()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'Barbados'
    assert response[0]['Status'] == 'deaths'

def test_with_status_recovered():
    country_instance = Covid('barbados', 'recovered')
    response = country_instance.cases_by_country()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'Barbados'
    assert response[0]['Status'] == 'recovered'


def test_cases_since_day1():
    country_instance = Covid('togo')
    response = country_instance.total_cases_since_day1()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'Togo'
    assert response[0]['Status'] == 'confirmed'
