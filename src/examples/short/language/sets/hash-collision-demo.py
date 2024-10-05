import random
import string


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def hash_collision_demo(num_strings, string_length):
    hashes = {}
    collisions = 0
    for _ in range(num_strings):
        s = generate_random_string(string_length)
        h = hash(s)
        if h in hashes:
            collisions += 1
        else:
            hashes[h] = s
    return collisions, len(hashes)


def main():
    num_strings = 1_000_000  # Number of strings to generate
    string_length = 10       # Length of each string
    collisions, unique_hashes = hash_collision_demo(num_strings, string_length)
    print(f"Total strings generated: {num_strings}")
    print(f"Number of unique hashes: {unique_hashes}")
    print(f"Number of collisions: {collisions}")
    print(f"Collision rate: {collisions / num_strings:.6%}")


if __name__ == "__main__":
    main()
