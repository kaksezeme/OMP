def get_input_arrays(file_path):
    inputs = []
    i = 0
    with open(file_path, "r") as lines:
        for line in lines:
            i = i + 1
            if line.find("#") != -1:
                line = line[:line.find("#")]
            if len(line) > 0:
                line = line.strip()
                line = line.replace("(", "")
                line = line.replace(")", "")
                line = line.replace(",", " ")
                line = line.split(" ")
                if len(line) == 8:
                    try:
                        line = list(map(lambda x: float(x), line))
                        inputs.append(line)
                    except ValueError:
                        print("Nisu uneseni brojevi")
                        continue
                else:
                    print("Unos je u krivome formatu linija [" + str(i) + "]")
                    continue
    return inputs