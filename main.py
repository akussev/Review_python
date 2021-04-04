import sys
import program

my_program = program.Program()

sys.argv.pop(0)
my_program.do_crypt(sys.argv)
