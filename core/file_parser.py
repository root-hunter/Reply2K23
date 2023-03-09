
def parse_file(filename="test_files/file.txt"):
    data = {}

    with open(filename, "r") as file:
        rows = file.read().split("\n")

        first_row = rows[0].split(" ")
        
        data["R"] = int(first_row[1])
        data["C"] = int(first_row[0])

        data["S"] = int(first_row[2])
        data["snakes"] = [int(x) for x  in rows[1].split(" ")]

        data["matrix"] = []
        data["wormhall"] = []

        for i in range(2, len(rows)):
            tmp = []
            r = rows[i].split(" ")
            for j in range(len(r)):
                if r[j] == "*":
                    data["wormhall"].append((j, i - 2))
                    tmp.append(0)
                else:
                    tmp.append(int(r[j]))
                    
            data["matrix"].append(tmp)
        
        file.close()
    return data
