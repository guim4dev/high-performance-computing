import subprocess


def compile_file(compiled_file: str, extra_flags: str = "") -> None:
    subprocess.call(
        f"g++ {extra_flags} -o {compiled_file} ./laplace.cxx",
        shell=True
    )
    
def write(process, message):
    process.stdin.write(f"{message.strip()}\n".encode("utf-8"))
    process.stdin.flush()
    
def run(run_file: str, output_file: str) -> None:
    with open(output_file, "w") as data_file:
        data_file.write("")
        data_file.close()
        
    with open(output_file, "a") as data_file:
        print(f"Writing to {output_file}...")
        for nx in [512, 1024, 2048]:
            print(f"Running for nx={nx}")
            with subprocess.Popen(run_file, stdin=subprocess.PIPE, stdout=data_file) as process:
                write(process, f"{nx} 1000 1e^-16")
        
        
def main() -> None:
    # Declare the calls
    # no flags call, -O3 call, -fopenmp call, -03 + -fopenmp call
    calls = [
        {
            "output_file": "./logs/noFlags.log",
            "compilation_dest": './executables/laplace_no_flags',
            "extra_flags": ""  
        },
        {
            "output_file": "./logs/vectorized.log",
            "compilation_dest": './executables/laplace_vectorized',
            "extra_flags": "-O3"  
        },
        {
            "output_file": "./logs/parallelism.log",
            "compilation_dest": './executables/laplace_parallelism',
            "extra_flags": "-fopenmp"  
        },
        {
            "output_file": "./logs/vectorized_parallelism.log",
            "compilation_dest": './executables/laplace_vectorized_parallelism',
            "extra_flags": "-O3 -fopenmp"
        }
    ]
    
    for call in calls:
        extra_flags= call["extra_flags"]
        print(f"Running with extra_flags={extra_flags or None}")
        compiled_file_dest = call["compilation_dest"]
        compile_file(compiled_file_dest, extra_flags)
        run(compiled_file_dest, call["output_file"])


if __name__ == "__main__":
    main()
