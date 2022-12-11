# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

"""
def get_test_file_from_pickle(name_file):
    import pandas as pd
    import pickle
    if name_file == "mcpas":
        data_file = open("Samples/mcpas_test_samples.pickle", 'rb')
        list_columns = ["TRA", "TRB", "TRAV", "TRAJ", "TRBV", "TRBJ", "T-Cell-Type", "Peptide", "MHC", "Sign"]
    elif name_file== "vdjdb":
        data_file = open("Samples/vdjdb_no10x_test_samples.pickle", 'rb')
        list_columns = ["TRB", "TRA", "TRAV", "TRAJ", "TRBV", "TRBJ", "Peptide", "MHC", "T-Cell-Type", "Sign"]
    else:
        raise ValueError
    data = pickle.load(data_file)
    df = pd.DataFrame(data).drop(["protein"], axis=1)
    print(df.columns)
    df.columns = list_columns
    print(df.columns)
    print(df)
    df.to_csv(name_file+"_test_with_sign.csv", index_label=False)
    df_without_sigh = df.drop(["Sign"], axis=1)
    df_without_sigh.to_csv(name_file+"_test.csv", index_label=False)
"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #get_test_file_from_pickle("mcpas")
    #get_test_file_from_pickle("vdjdb")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

