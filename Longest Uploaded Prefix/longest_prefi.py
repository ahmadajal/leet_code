import bisect 

class LUPrefix:

    def __init__(self, n: int):
        self.num_videos = n
        self.uploaded = list()
        self.start = 1

    def upload(self, video: int) -> None:
        bisect.insort(self.uploaded, video)

    def longest(self) -> int:
        if not self.uploaded:
            return 0
        elif self.uploaded[0] != 1:
            return 0
        else:
            for i in range(self.start-1, len(self.uploaded)):
                if self.uploaded[i] == i+1:
                    self.start = i+1
                else:
                    break
            return self.start

        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()