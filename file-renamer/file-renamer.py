import os

def rename_files_in_directory():
    path = r"C:/Users/lspencer1/OneDrive - Department for Education\Documents/Team/Test"
    replacements = ["_dualforecast", "_narrative", "_pf1", "_summary", "_txn"]
    search_terms = ["CLAIM", "NARRATIVE", "PF1", "SUMMARY", "Txn"]

    os.chdir(path)
    count = 0
    i = 0
    
    for file in os.listdir():
        name, extension = os.path.splitext(file)

        for j, term in enumerate(search_terms):
            if term in name:
                prefix = name[:11]
                postfix = replacements[j]
                new_name = prefix + postfix + extension
                os.rename(file, new_name)

        count += 1
        i += 1

        if i > 4:
            i = 0

    
    print(f"{count} files in folder {path} were renamed.")


if __name__ == "__main__":
    rename_files_in_directory()