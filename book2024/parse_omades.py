def parse_omades(filename):
    omades = []
    with open(filename, encoding="utf-8") as file:

        for line in file.readlines():

            line = line.strip()

            if len(line) < 3:
                continue

            omada, typos = line.split()
            omades.append((omada, typos))

    return omades
