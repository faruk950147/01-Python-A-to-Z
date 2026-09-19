class RunnerUp:
    def __init__(self):
        pass

    def find_runner_up(self, scores):
        scores = list(set(scores))
        scores.sort()

        return scores[-2]

    def find_runner_up1(self, scores):
        scores.sort(reverse=True)

        for i in range(len(scores) - 1):
            if scores[i] != scores[i + 1]:
                return scores[i + 1]


if __name__ == "__main__":
    n = int(input("How many numbers: "))
    scores = list(map(int, input().split()))

    runner_up = RunnerUp()
    result = runner_up.find_runner_up1(scores)

    print("Runner-up score:", result)