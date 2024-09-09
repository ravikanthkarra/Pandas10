import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    group = daily_sales.groupby(['date_id', 'make_name'])
    result = group.agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    ).reset_index()
    return result
    # dict = {}
    # for i in range(len(daily_sales)):
    #     dateid = daily_sales['date_id'][i]
    #     make = daily_sales['make_name'][i]
    #     leadid = daily_sales['lead_id'][i]
    #     partnerid = daily_sales['partner_id'][i]
    #     keytup = (dateid, make)
    #     if keytup not in dict:
    #         dict[keytup] = []
    #         (dict[keytup]).append({leadid})
    #         (dict[keytup]).append({partnerid})
    #     else:
    #         (dict[keytup])[0].add(leadid)
    #         (dict[keytup])[1].add(partnerid)
    # # print(dict)
    # result = []
    # for key, value in dict.items():
    #     result.append([key[0], key[1] , len(value[0]), len(value[1])])
    # # print(result)

    # df = pd.DataFrame(result, columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners'])
    # return df

