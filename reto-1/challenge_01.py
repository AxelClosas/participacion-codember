def frecuencia(path):
    f = {}
    with open(path, "r") as file:
        my_list = [words.lower() for words in file]
        my_list = my_list[0].split()
        for word in my_list:
            if word in f.keys():
                f[word] += 1
            else:
                f[word] = 1
        keys = list(f.keys())
        values = list(f.values())
        result = "".join(list(map(lambda x, y: str(x) + str(y), keys, values)))

    return result


def run():
    result = frecuencia("./message_01.txt")
    print(result)


if __name__ == "__main__":
    run()
