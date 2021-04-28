import api_helper
import data_helper
import enums
import file_helper
import visualize


def engine():
    data = api_helper.fetch_data()         # Get data
    data_set = data_helper.make_df(data)   # Transform data
    file_helper.make_target_file(data_set) # Make a dump file
    visualize.visualize(data_set)          # Visualize the data

engine()