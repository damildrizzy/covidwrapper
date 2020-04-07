from covidwrapper import Covid

def test_live_cases():
    country_instance = Covid('south-africa')
    response = country_instance.live_cases_by_country()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'South Africa'

def test_live_cases_status():
    country_instance = Covid('switzerland', 'recovered')
    response = country_instance.live_cases_by_country()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'Switzerland'
    assert response[0]['Status'] == 'recovered'

def test_live_cases_since_day1():
    country_instance = Covid('italy', 'deaths')
    response = country_instance.live_cases_since_day1()

    ssert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'Italy'
    assert response[0]['Status'] == 'recovered'
