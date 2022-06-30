from roku_api.exceptions import ChannelNotInstalledError, FeatureNotSupported
def test():
    if ('9.2' < '9.3'):
        raise FeatureNotSupported(
            'FW 9.3 or later required for query-home-screen-menu ECP command'
        )


def test2():
    try:
        test()
    except FeatureNotSupported:
        print("raised error")

    
def main():
    test2()
  

if __name__ == '__main__':
    main()