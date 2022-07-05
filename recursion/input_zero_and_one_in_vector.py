n = 3
result_vector = [0] * n


def generate_vector(idx, vector):
    if idx >= len(vector):
        print(vector)
        return
    for num in range(2):
        vector[idx] = num
        generate_vector(idx + 1, vector)


if __name__ == '__main__':
    generate_vector(0, result_vector)