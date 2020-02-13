
def to_c(from_f):
    celsius = (from_f - 32) * (5 / 9)
    return celsius


# Main Routine
temperatures = [0, 40, 100]
converted = []


for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statement)


print(converted)
