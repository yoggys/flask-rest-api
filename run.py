import asyncio

from core.setup import Server
from core.utils import parse_args

def main():
   args = parse_args()
   
   server = Server(args)
   server.run()

if __name__ == '__main__':
   main()