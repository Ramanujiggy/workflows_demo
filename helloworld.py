import sys

def main():
    print("Hello world! From Python: " +str(sys.version_info))
    if sys.version_info >= (3,6) and sys.version_info < (3,7):
        #lets make this script fail for python 3.6
        raise Exception('Python version 3.6x is unsupported!')



if __name__== "__main__":
    main()
        
