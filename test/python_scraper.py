def save_trading_report(trading_report: list, news_data):
    data_to_save = []
    for report in trading_report:
        data_to_save.append(report.text)
    report = TradingReport()
    report.company_title = data_to_save[0].replace("‏", '').replace(" ",'').strip()
    report.company_name = data_to_save[1].replace("‏", '').replace(" ",'').strip()
    report.buy_volume = data_to_save[2].replace("‏", '').replace(" ",'').replace(",",'').replace(" ",'')
    report.sell_volume = data_to_save[3].replace("‏", '').replace(" ",'').replace(",",'').replace(" ",'')
    report.report_data = datetime.datetime.strptime(f"{news_data}T10:10:10-0005", '%Y-%m-%dT%H:%M:%S%z')
    session.add(report)
    session.commit()