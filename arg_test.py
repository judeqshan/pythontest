# import argparse

# def add(args):
#      r = args.x + args.y
#      print('x + y = ', r)

# def sub(args):
#      r = args.x - args.y
#      print('x - y = ', r)

# parser = argparse.ArgumentParser(prog='PROG')
# subparsers = parser.add_subparsers(help='sub-command help')
# #添加子命令 add
# parser_a = subparsers.add_parser('add', help='add help')
# parser_a.add_argument('-x', type=int, help='x value')
# parser_a.add_argument('-y', type=int, help='y value')
# #设置默认函数
# parser_a.set_defaults(func=add)
# #添加子命令 sub
# parser_s = subparsers.add_parser('sub', help='sub help')
# parser_s.add_argument('-x', type=int, help='x value')
# parser_s.add_argument('-y', type=int, help='y value')
# #设置默认函数
# parser_s.set_defaults(func=sub)
# args = parser.parse_args()
# #执行函数功能
# args.func(args)


import argparse
import sys
from atoi import atoi

def get_args(cmdline_args=None):
     atoi("12")
     parse = argparse.ArgumentParser()
     parse.add_argument("-t", "--time_name", help="time name")
     parse.add_argument("-p", "--port", action='append', help="port")
     args = parse.parse_args(args=cmdline_args)

     print(args.time_name)
     print("---------------\n")
     print(args.port)

def execute(args=None):
    """Loads devices and runs tests."""
    if (args is None):
        try:

            args = get_args()

        except argparse.ArgumentError:
            return 

def main():
    """This is the *real* main method (to handle setup.py directing the entry point here). This
    is a thin wrapper around execute() so that we can do some final error handling

    """
    for i in range(1,5):
        print(i)
    try:

        sys.exit(execute())

    except Exception:  # pylint: disable=broad-except

          print("exception")

    finally:
          print("finally")

if (__name__ == '__main__'):  # pragma: no cover
    main()

