import math

def entropy(data, targetparam):
    freq = {}
    entropy = 0.0

    for record in data:
        if (freq.has_key(record[targetparam])):
            freq[record[targetparam]] += 1.0
        else:
            freq[record[targetparam]] = 1.0

    for freq in freq.values():
        entropy += (-freq / len(data)) * math.log(freq / len(data), 2)

    return entropy
