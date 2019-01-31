def write_to_file(directory, file_name, params, data, max):
    """
    """

    with open(directory + file_name + '_' + '_'.join(params) + '.csv', 'w') as file:
        for i, test_data in enumerate(data):
            if i > max:
                break
            for j, preferences in enumerate(test_data):
                file.write('[')
                for k, preference in enumerate(preferences):
                    file.write('{:.4f}'.format(preference))
                    if k != len(preferences) - 1:
                        file.write(',')
                file.write(']')
                if j != len(test_data) - 1:
                    file.write(',')
            if i != len(test_data) - 1:
                file.write('\n')