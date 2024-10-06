# This program is used for easily adding entries to the csv file with ships

from pandas import read_csv

FILENAME = "shipping_chart.csv"
INCLUDE_COMMENTS = True

df = read_csv(FILENAME, comment="#")

personality_types = list(df.columns)[1:]

while True:
    new_row = []

    while True:
        input_type = input("Enter the personality type of the user: ")
        input_type = input_type.upper()
        if input_type in personality_types:
            break
        print("Incorrect input")
    
    new_row.append(input_type)

    for type in personality_types:
        print(type)
        values = [0,0,0,0,0,0,0]
        while True:
            while True:
                option = input("choose option (otp, cute, brotp, platonic, neutral, dislike, stop, exit): ")
                option = option.lower()
                if option in ["otp","cute","brotp","platonic","neutral","dislike","stop","exit", "paltonic"]:
                    break
                print("Incorrect option")
            if option == "exit":
                break
            elif option == "otp":
                values[0] += 1
            elif option == "cute":
                values[1] += 1
            elif option == "brotp":
                values[2] += 1
            elif option == "platonic" or option == "paltonic":
                values[3] += 1
            elif option == "neutral":
                values[4] += 1
            elif option == "dislike":
                values[5] += 1
            elif option == "stop":
                values[6] += 1
            else:
                print("Error: cannot interpret option")
        values = list(map(str, values))
        new_row.append(";".join(values))
    
    df.loc[len(df)] = new_row

    if INCLUDE_COMMENTS:
        with open(FILENAME, "w") as f:
            f.write("# types ships counts are in order of: otp;cute/like;brotp;platonic;don't care/neutral;dislike;make it stop\n")
            f.write("# file compiled by u/KomornikBank\n")
    df.to_csv(FILENAME, mode="a", index=False)