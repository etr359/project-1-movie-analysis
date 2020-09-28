def clean_convert_gross(x):
    """Check if value is a string, if True, check for comma.
    If True remove comma and convert to float. If False, return float 
    and divide by 1 million otherwise the value is numeric."""
    if isinstance(x, str):
        if ',' in x:
            billion = x.replace(',','')
            return float(billion)
        if ',' not in x:
            return (float(x))/1000000
    return(x)