from my_utils import summarize

if __name__ == '__main__':
    data = [1, 2, 3.4, 'Vinod', False, 40]
    a, b, c, d = summarize(data)

    print(f'{a = }\n{b = }\n{c = }\n{d = }\n')