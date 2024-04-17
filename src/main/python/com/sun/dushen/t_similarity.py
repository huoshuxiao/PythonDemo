from concurrent import futures

from com.sun.dushen.model.lottery import similarity


def main():

    for i in range(0, 50):
        # TODO
        # count = [8749216, 18080715]
        # count = [2603036]
        count = [354432, 21265920]
        with futures.ProcessPoolExecutor(len(count)) as executor:
            fs = []
            for i in range(0, len(count)):
                f = executor.submit(similarity.run, count[i])
                fs.append(f)

            for f in futures.as_completed(fs):
                f.result()


if __name__ == '__main__':
    main()
