def get_cats_info(path: str):
    try:
        with open(path, "r", encoding="UTF-8") as list_cats:
            outlist = []
            for line in list_cats:
                line = line.split(",")
                outlist.append({"id": line[0], "name": line[1], "age": line[2]})
    except FileNotFoundError:
        print(f"File {path} not found.")
        return None
    except Exception:
        print("The file is in the wrong format or is empty.")
        return None

    print(f"[{', '.join(map(str, outlist))}]")

path_to_file = './GOIT-ALGO-HW-04/cats_info.txt'
get_cats_info(path_to_file)