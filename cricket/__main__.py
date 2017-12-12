from .stats import parse_args


def main():
    args = parse_args()
    args.func()


if __name__ == '__main__':
    main()
