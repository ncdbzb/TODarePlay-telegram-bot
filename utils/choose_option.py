from random import sample


def get_que_act(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        split_file = list(filter(None, file.read().split('\n')))

    return sample(split_file, 1)[0]
