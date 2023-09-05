from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        self.t = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append(value)
        self.t[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.t:
            return ""
        time_list = self.t[key]
        if timestamp > time_list[-1]:
            return self.d[key][-1]
        elif timestamp < time_list[0]:
            return ""
        else:
            start = 0
            end = len(time_list) - 1
            while start <= end:
                mid = (start+end)//2
                if time_list[mid] == timestamp:
                    return self.d[key][mid]
                elif time_list[mid] > timestamp:
                    end = mid - 1
                else:
                    start = mid + 1
            if time_list[mid] <= timestamp:
                return self.d[key][mid]
            else:
                return self.d[key][mid-1]