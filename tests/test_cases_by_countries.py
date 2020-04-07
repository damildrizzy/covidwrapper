from covidwrapper import Covid

def test_cases_by_countries():
    barbados = Covid('barbados')
    response = barbados.cases_by_country()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert response[0]['Country'] == 'Barbados'