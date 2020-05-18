# -*- coding: utf-8 -*-
from directory import Directory


def main():
    d = Directory()
    folder = d.get_folder_from_user()
    folder_contents = d.get_folder_contents(folder)
    table_name = d.get_table_name()
    df = d.merge_all_tables(folder_contents, table_name)
    df.to_csv('../merged_tables.csv')


if __name__ == "__main__":
    main()
