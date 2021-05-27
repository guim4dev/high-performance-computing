import subprocess
from psutil import cpu_count
from glob import glob
import os

number_of_threads = cpu_count(logical=True)

def compile_file(compiled_file: str, orig_file: str, extra_flags: str = "") -> None:
    subprocess.call(
        f"g++ {extra_flags} -o {compiled_file} {orig_file}",
        shell=True
    )
    
def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()

def run_paralelized(run_file, output_file, data_file, nx) -> None:
    for n_threads in range(1, number_of_threads+1):
        print(f"Running for {n_threads} threads...")
        os.environ["OMP_NUM_THREADS"] = str(n_threads)
        with subprocess.Popen(run_file, stdin=subprocess.PIPE, stdout=data_file) as process:
            write(process, f"{nx} 1000 1e^-16")
            response = process.wait()
            print(f"Process response was {response}")

def run(run_file: str, output_file: str) -> None:
    with open(output_file, "w") as data_file:
        data_file.write("")
        data_file.close()
        
    with open(output_file, "a") as data_file:
        print(f"Writing to {output_file}...")
        for nx in [512, 1024, 2048]:
            print(f"Running for nx={nx}")
            if run_file in ['./executables/laplace_parallelism', './executables/laplace_vectorized_parallelism']:
                run_paralelized(run_file, output_file, data_file, nx)
                continue
            
            with subprocess.Popen(run_file, stdin=subprocess.PIPE, stdout=data_file) as process:
                write(process, f"{nx} 1000 1e^-16")
                response = process.wait()
                print(f"Process response was {response}")
        
        
def main() -> None:
    # Declare the calls
    # no flags call, -O3 call, -fopenmp call, -03 + -fopenmp call
    calls = [
        {
            "output_file": "./data/noFlags.csv",
            "compilation_dest": './executables/laplace_no_flags',
            "extra_flags": "",
            "compilation_orig": "./laplace_original.cxx"
        },
        {
            "output_file": "./data/vectorized.csv",
            "compilation_dest": './executables/laplace_vectorized',
            "extra_flags": "-O3",
            "compilation_orig": "./laplace_original.cxx"
        },
        {
            "output_file": "./data/parallelism.csv",
            "compilation_dest": './executables/laplace_parallelism',
            "extra_flags": "-fopenmp",
            "compilation_orig": "./laplace.cxx"
        },
        {
            "output_file": "./data/vectorized_parallelism.csv",
            "compilation_dest": './executables/laplace_vectorized_parallelism',
            "extra_flags": "-O3 -fopenmp",
            "compilation_orig": "./laplace.cxx"
        }
    ]
    
    for call in calls:
        extra_flags= call["extra_flags"]
        print(f"Running with extra_flags={extra_flags or None}")
        compiled_file_dest = call["compilation_dest"]
        compile_file(compiled_file_dest, call["compilation_orig"], extra_flags)
        run(compiled_file_dest, call["output_file"])

    data = 'nx, time, n_threads, result, origin_file\n'
    for file in glob("./data/*.csv"):
        with open(file, "r") as current_file:
            lines = current_file.readlines()
            for index in range(len(lines)):
                line_as_list = lines[index].split(',')
                line_as_list[-1] = line_as_list[-1].rsplit('\n')[0]
                line_as_list.append(file.split('data/')[1])
                lines[index] = ",".join(line_as_list) 
            data += "\n".join(lines)
            data += "\n"
            
    
    with open('./data.csv', "w") as data_file:
        data_file.write(data)
        data_file.close()


if __name__ == "__main__":
    main()
