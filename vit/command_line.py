import signal
from vit import parse_options, Application


def handler(signum, frame):
    pass


signal.signal(signal.SIGINT, handler)


def main():
    options, filters = parse_options()
    Application(options, filters)


if __name__ == '__main__':
    main()
