# Methods for Data Exploration

def find_csv_col_by_metric(df, metric):
    """
    Finds columns based on metric. Must be column with .csv at end
    @returns list of column names with metric
    """
    all_columns = df.columns
    found = []
    
    for col in all_columns:
        if col.endswith(metric+".csv"):
            found.append(col)
    return found