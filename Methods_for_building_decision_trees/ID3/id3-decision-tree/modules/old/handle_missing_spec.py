def attribute_mode(data_set, attribute):
    """Returns the mode value of an attribute among a subset of examples.

    Arguments:
        data_set {List of Examples}
        attribute {Int} -- the index of the attribute of interest

    Returns:
        {String} -- the attribute value with the most instance matches
    """

    # Use a dictionary to keep track of attribute values
    values = {}

    for x in data_set:
        a = x[attribute]
        if a is not None:
            if a in values.keys():
                values[a].append(x)
            else:
                # Add value to dictionary
                values[a] = [x]

    # Return the value with the most instance matches among the dataset
    try:
        mode = max(values.items(), key=lambda x: len(x[1]))[0]
    except (ValueError):
        # Just assign "None"
        mode = None

    return mode


def attribute_mean(data_set, attribute):
    """Computes the mean value for a given attribute among examples in the data set.

    Arguments:
        data_set {List of Examples}
        attribute {Int} -- the index of the attribute of interest

    Returns:
        {Float} -- the average attribute value
    """

    filtered_data = [x for x in data_set if x[attribute] is not None]

    if filtered_data:
        s = sum([x[attribute] for x in filtered_data])
        mean = s / float(len(filtered_data))
    else:
        mean = 0

    return mean


def handle_missing(data_set, attribute_metadata, attribute):
    """Handles missing attribute values in dataset.

    For a nominal attribute, assigns the most common attribute value among examples in the dataset.
    For a numerical attribute, assigns the weighted average attribute value among examples in the

    Arguments:
        data_set {List of Examples}
        attribute_metadata {List of Dictionaries}
        attribute {Int} -- the index of the attribute of interest

    Returns:
        {List of Examples} -- a deepcopy of the dataset with missing attributes replaced accordingly
    """

    replaced_data = deepcopy(data_set)

    if attribute_metadata[attribute]["is_nominal"]:
        replacement = attribute_mode(data_set, attribute)
    else:
    # Attribute is numerical, so substitute the mean
        replacement = attribute_mean(data_set, attribute)

    for x in replaced_data:
        if x[attribute] is None:
            x[attribute] = replacement

    return replaced_data