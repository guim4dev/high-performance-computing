import subprocess


def run_dinamically(state: list[int], language: str) -> list[int]:
    size = state[0]
    increment = state[1]
    ret_code = 0
    while ret_code == 0:
        ret_code = subprocess.call(
            [f"./{language}_resolution/resolution", str(size)]
        )
        size = size + increment
    return [size, increment]


def process(language: str, compiler_call: str) -> str:
    compile = subprocess.call(
        compiler_call,
        shell=True,
    )

    if compile != 0:
        raise RuntimeError(f"Couldnt compile {language} file")

    state = [1, 10000]
    while state[1] > 1:
        state = run_dinamically(state, language, data_file)
        state[0] = state[0] - state[1]
        state[1] = state[1]//2
    print(f"Max N value for language {language} is {state[0]}")
    return "done"


def main():
    # First, discover for C solution
    process(
        language="c",
        compiler_call="gcc -Wall -o ./c_resolution/resolution ./c_resolution/resolution.c",
    )
    # Then, discover for FORTRAN solution
    process(
        language="fortran",
        compiler_call="gfortran ./fortran_resolution/resolution.f95 -o ./fortran_resolution/resolution",
    )


if __name__ == "__main__":
    main()
