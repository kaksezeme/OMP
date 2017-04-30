def get_input_arrays(file_path):
    """
    Dohvacanje podataka iz datoteke u formatu (x1,y1) (x2,y2) (x3,y3) (x4,y4)
    Podaci iza # se ne uzimaju u obzir i predstavljaju komentar unutar datoteke
    :param file_path: putanja do dadoteke u kojoj se nalaze tocke
    :return: array - lista kordinata jednog unosta
    :except ValueError - Ako jedan od {x1,y1,x2,y2,x3,y3,x4,y4} nije broj
    """
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
