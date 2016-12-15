from entropy import entropy


def informationgain(data, param, targetparam):
    freq = {}
    subentropy = 0.0

    for i in data:
        if (freq.has_key(i[param])):
            freq[i[param]] += 1.0
        else:
            freq[i[param]] = 1.0

    for val in freq.keys():
        val_prob = freq[val] / sum(freq.values())
        data_subset = [i for i in data if i[param] == val]
        subentropy += val_prob * entropy(data_subset, targetparam)

    return (entropy(data, targetparam) - subentropy)
