if __name__ == '__main__':
   import server, client
   import sys

   if sys.argv[1] == 'server':
      server.run()
   elif sys.argv[1] == 'client':
      client.run()
