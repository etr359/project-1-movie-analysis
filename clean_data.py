def gross_converter(gross):
    """Takes in string value with comma and ., removes comma, converts to float
    and multiplies by 1 million"""
    for g in gross:
        try:
            if ',' not in g:
                no_comma_gross = float(g)
                return no_comma_gross / 1000000
            else:
                comma_gross = g.str.replace(',','')
                return float(g)
        except TypeError:
            continue
