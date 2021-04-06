from typing import List, Dict
# def indent(size, content: List[str]):

def indent(size, content):
    print(f'This is output of {len(content)} lines')
    for line in content:
        print(size * '.' + line)


indent(3, 'micka masa mirek')
indent(3, 'micka masa mirek'.split())


def indent_dict(content: List[Dict[str, int]]):
    for item in content:
        for key, value in item.items():
            print(key)
            c = value / 2
            print(c)


dict_content = [
    # vs {'age': '5'},
    {'age': 5},
]

indent_dict(dict_content)