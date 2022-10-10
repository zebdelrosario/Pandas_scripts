"""Pandas Scripts for data analysis.
Dev Start:  29/09/22
Lead Dev:   Zeb del Rosario
"""
import pandas as pd


def main():
    """Main code block."""
    filename = input("Enter filename: (Do not add extension)\n>")
    sheet_name = input("Enter sheet name:\n>")
    ticket_excel_file = pd.read_excel(f'files/{filename}.xlsx', sheet_name=sheet_name)
    issue_types = get_issue_types(ticket_excel_file, 'Issue Type')
    display_all_issue_types(issue_types, ticket_excel_file)


def display_all_issue_types(issue_types, dataframe):
    """Displays a summary of all issues types."""
    for issue in issue_types:
        hours_worked = sum_column(dataframe, 'Issue Type', issue, 'Total Hours Worked')
        total_count = count_column(dataframe, 'Issue Type', issue, 'Total Hours Worked')
        print(f"""{issue:<17} Hrs: {hours_worked:<8.1f} Count: {total_count}""")


def get_issue_types(dataframe, issue_column):
    """Return all the types of issues that occurred for the df."""
    issue_types = []
    for i in dataframe[issue_column]:
        if i not in issue_types:
            issue_types.append(i)
    return issue_types


def sum_column(dataframe, read_column, read_keyword, write_column):
    """Sum column values based on keyword."""
    return dataframe.loc[dataframe[read_column] == read_keyword, write_column].sum()
    # return dataframe.groupby(read_column)[write_column].sum()  Alternative method (Group By)


def count_column(dataframe, read_column, read_keyword, write_column):
    """Sum column values based on keyword."""
    return dataframe.loc[dataframe[read_column] == read_keyword, write_column].count()
    # return dataframe.groupby(read_column)[write_column].count()  Alternative method (Group By)


if __name__ == "__main__":
    main()