import commands


def main():
    args = commands.parse_args()
    args.func()


if __name__ == '__main__':
    main()
