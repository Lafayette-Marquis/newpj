program hello
  ! This is a comment line; it is ignored by the compiler
  print *, 'Hello, World!'
  implicit none

  integer :: amount
  real :: pi
  complex :: frequency
  character :: initial
  logical :: isOkay
  amount = 10
  pi = 3.1415927
  frequency = (1.0, -0.5)
  initial = 'A'
  isOkay = .false.
  print *, amount, pi, frequency, initial, isOkay
end program hello