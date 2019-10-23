from index_derivative_historical_options \
    import IndexDerivativeHistoricalOptions

derivative_historical_options = IndexDerivativeHistoricalOptions('BANKNIFTY')
derivative_historical_options.get_available_years()
derivative_historical_options.get_available_expiry_dates()
derivative_historical_options.get_available_strike_prices(option_type='Call')
# derivative_historical_options.get_available_strike_prices(option_type='Put')
derivative_historical_options.download_data_for_each_strike_price(option_type='Call')
# derivative_historical_options.download_data_for_each_strike_price(option_type='Put')
