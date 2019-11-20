def check_float(inputValue):
    # Sprawdzanie czy podana zostala liczba
    try:
        value = float(inputValue)
        status = 'success'
    except ValueError:
        print('Zly format danych. Wprowadz liczbe')
        status = 'fail'

    return(status)
