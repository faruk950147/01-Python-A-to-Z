class RunnerUp:
    def __init__(self, scores):
        self.scores = scores

    def find_runner_up(self):
        unique_scores = list(set(self.scores))
        unique_scores.sort()

        return unique_scores[-2]

if __name__ == "__main__":
    n = int(input("How many numbers: "))
    scores = list(map(int, input().split()))

    obj = RunnerUp(scores)

    print(obj.find_runner_up())