from pathlib import Path
import os

def csv_analysis():
    d = os.getcwd()

    file_to_open = os.path.join(d, "techcruch.csv")
    print(file_to_open)

    lines = (line for line in open(file_to_open))
    list_line = (s.rstrip().split(',') for s in lines)
    cols = next(list_line)
    print(cols)
    assert "round" in cols

    company_dicts = (dict(zip(cols, data)) for data in list_line)

    funding = ( 
        int(company_dicts["raiseAmt"])
        for company_dict in company_dicts
        if company_dict["round"] == "a"
    )

    total_series_a = sum(funding)
    print(f"Total series A fundraising: ${total_series_a}")

if __name__ == "__main__":
    csv_analysis()