import pandas as pd

def csv(inp):
    
    Data = {'File': [i[0] for i in inp],
        'Name': [i[1] for i in inp],
            'Cashier': [i[2] for i in inp],
            'Date': [i[3] for i in inp],
            'Total': [i[4] for i in inp],
            }

    df = pd.DataFrame(Data)
    df.to_csv('Output.csv', index=False)
    return Data
