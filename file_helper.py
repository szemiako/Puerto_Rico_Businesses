import data_helper
import enums

def make_target_file(data_set, path=enums.attributes()._default_path, extension=enums.attributes()._extension, delimiter=enums.attributes()._delimiter, properties=enums.enums()._properties):  
    data_file = open('{0}data_file{1}'.format(path, extension), 'w')
    data_file.write('{header}\n'.format(header = delimiter.join(properties)))
    return data_set.to_csv(
        data_file,
        quoting=2,
        header=False,
        index=False,
        line_terminator='\n',
        sep=delimiter
    )