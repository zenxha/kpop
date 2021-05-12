import datetime

class game:
    def __init__(self, title,releasedate,randomfact=None):
        self._title = title
        self._releasedate = releasedate
        self._randomfact = randomfact

    def calculateage(self):
        release_obj = datetime.datetime.strptime(self._releasedate, '%Y-%m-%d')
        diff = datetime.datetime.now() - release_obj
        return diff
    def gettitle(self):
        return self._title
    def getreleasedate(self):
        return self._releasedate
    def getrandomfact(self):
        return self._randomfact

class CharlieBubbleSort:
    def __init__(self, input_list,isString):
        self.input_list = input_list
        self._output_list = []
        self.bubblesort(input_list)
        self.isString = isString

    def bubblesort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    def StringSort(self, arr):
        string = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'j', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X',
                  'Y','Z']
        for j in range(0, len(arr)):
            for i in range(0, len(arr)):
                _sorted = False
                if i != len(arr)-1:
                    for k in range(0,len(arr[i])):
                        if not _sorted:
                            if k != (len(arr[i]) and len(arr[i+1])):
                                if string.index(arr[i][k]) > string.index(arr[i+1][k]):
                                    arr[i], arr[i+1] = arr[i+1], arr[i]
                                    _sorted = True
                                elif string.index(arr[i][k]) < string.index(arr[i+1][k]):
                                    _sorted = True
                                else:
                                    if len(arr[i+1]) < len(arr[i]):
                                        arr[i], arr[i+1] = arr[i+1], arr[i]
                                        _sorted = True
    def ConvertString(self,arr):
        for j in range(0, len(arr)):
            arr[j] = arr[j].upper()


    @property
    def OutputList(self):
        arr = self.input_list
        if(self.isString):
            self.ConvertString(arr)
            self.StringSort(arr)
            for i in range(len(arr)):
                self._output_list.append(arr[i])
            return self._output_list
        else:
            self.bubblesort(arr)
            for i in range(len(arr)):
                self._output_list.append(arr[i])
            return self._output_list
