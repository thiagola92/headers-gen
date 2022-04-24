from unittest import main, TestCase

from la_headers.config import generate_random_config


class TestSystem(TestCase):
    def test_base(self) -> None:
        print(generate_random_config())
        print(generate_random_config())
        print(generate_random_config())
        print(generate_random_config())
        print(generate_random_config())
        print(generate_random_config())
        print(generate_random_config())


if __name__ == "__main__":
    main()
