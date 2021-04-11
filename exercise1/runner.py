import subprocess
import pandas as pd
import matplotlib.pyplot as plt


def process_c_resolution() -> None:
    data_file_path = "./c_resolution/data.csv"
    data_file = open(data_file_path, "a")
    subprocess.call(
        "gcc -Wall -o ./c_resolution/resolution ./c_resolution/resolution.c", shell=True
    )
    size = 1
    while size <= 36000:
        ret_code = subprocess.call(
            ["./c_resolution/resolution", str(size)], stdout=data_file
        )
        size = size * 2
    data_file.close()
    return data_file_path


def generate_graph(file_path: str, plot_dest: str):
    dataframe = pd.read_csv(file_path)
    plt.plot("size", "i_first", data=dataframe, color="blue")
    plt.plot("size", "j_first", data=dataframe, color="red")
    plt.xlabel("N")
    plt.ylabel("time")
    plt.legend()
    plt.savefig(plot_dest)


def main():
    # First, run C solution
    data_file_path = process_c_resolution()
    generate_graph(data_file_path, "./plots/c_resolution.png")
    # Run Fortran solution
    # data_file_path = process_fortran_resolution()
    # generate_graph(data_file_path)


if __name__ == "__main__":
    main()