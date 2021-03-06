import subprocess
import pandas as pd
import matplotlib.pyplot as plt


def process(language: str, compiler_call: str) -> str:
    data_file_path = f"./{language}_resolution/data.csv"
    # create empty data file
    with open(data_file_path, "w") as data_file:
        data_file.write("")
        data_file.close()

    compile = subprocess.call(
        compiler_call,
        shell=True,
    )

    if compile != 0:
        raise RuntimeError(f"Couldnt compile {language} file")

    with open(data_file_path, "a") as data_file:
        size = 1
        while size < 42000:
            ret_code = subprocess.call(
                [f"./{language}_resolution/resolution", str(size)], stdout=data_file
            )
            size = size * 2
        subprocess.call(
            [f"./{language}_resolution/resolution", str(42000)], stdout=data_file
        )
    return data_file_path


def generate_graph(file_path: str, plot_dest: str) -> None:
    dataframe = pd.read_csv(file_path, delimiter=",")
    dataframe.columns = ["Matrix Dimension", "External i", "External j"]
    plt.plot("Matrix Dimension", "External i", data=dataframe, color="blue")
    plt.plot("Matrix Dimension", "External j", data=dataframe, color="red")
    plt.xlabel("N")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig(plot_dest)


def main():
    # First, run C solution
    data_file_path = process(
        language="c",
        compiler_call="gcc -Wall -o ./c_resolution/resolution ./c_resolution/resolution.c",
    )
    plt.figure(0)
    generate_graph(data_file_path, "./plots/c_resolution.png")
    # Then, run FORTRAN solution
    data_file_path = process(
        language="fortran",
        compiler_call="gfortran ./fortran_resolution/resolution.f95 -o ./fortran_resolution/resolution",
    )
    plt.figure(1)
    generate_graph(data_file_path, "./plots/fortran_resolution.png")


if __name__ == "__main__":
    main()
