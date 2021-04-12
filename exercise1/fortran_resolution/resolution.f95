program multiply_matrix_vector
    implicit none

    character(len=32) :: argument
    integer :: size
    real(8) :: before, after, diff_ij, diff_ji
    real(8), dimension(:,:), allocatable :: matrix
    real(8), dimension (:), allocatable :: vector
    real(8), dimension (:), allocatable :: result_vector

    call getarg(1, argument)
    read(argument, "(I10)") size
    call increment(size, 1)
    call random_seed()

    allocate(matrix(size, size))
    allocate(vector(size))
    allocate(result_vector(size))
    call spawn_random_matrix(matrix, size)
    call spawn_random_vector(vector, size)

    call cpu_time(before) 
    call multiply_first_i(matrix, vector, size, result_vector)
    call cpu_time(after)
    diff_ij = after - before

    call cpu_time(before) 
    call multiply_first_j(matrix, vector, size, result_vector)
    call cpu_time(after)
    diff_ji = after - before

    deallocate(matrix)
    deallocate(vector)
    deallocate(result_vector)

    print *,argument,",",diff_ij,",",diff_ji

    contains

    elemental subroutine increment(var, incr)
        implicit none
        integer,intent(inout) :: var
        integer,intent(in)    :: incr

        var = var + incr
    end subroutine

    subroutine spawn_random_vector(vector, size)
        implicit none
        real(8), dimension(:) :: vector
        integer :: size, i
        real(8) :: value
        do i=1, size
            call random_number(value)
            vector(i) = value * (size)
        end do 
    end

    subroutine spawn_random_matrix(matrix, size)
        implicit none
        real(8), dimension(:,:) :: matrix
        integer :: size, i, j
        real(8) :: value

        do i=1, size
            do j=1, size
                call random_number(value)
                matrix(i, j) = value * (size)
            end do
        end do
    end

    subroutine multiply_first_i(matrix, vector, size, result_vector)
        implicit none
        real(8), dimension (:) :: vector
        real(8), dimension (:, :) :: matrix
        real(8), dimension (:) :: result_vector
        integer :: i, j, size

        do i=1, size
            result_vector(i) = 0
            do j=1, size
                result_vector(i) = result_vector(i) +  vector(j)*matrix(i, j);
            end do
        end do
    end

    subroutine multiply_first_j(matrix, vector, size, result_vector)
        implicit none
        real(8), dimension (:) :: vector
        real(8), dimension (:, :) :: matrix
        real(8), dimension (:) :: result_vector
        integer :: i, j, size

        do j=1, size
            result_vector(j) = 0
            do i=1, size
                result_vector(i) = result_vector(i) +  vector(j)*matrix(i, j);
            end do
        end do
    end
end program multiply_matrix_vector

