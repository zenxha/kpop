import random


class top_5:
    def __init__(self, tracks):
        if len(tracks) < 0:
            raise ValueError("Songs must be greater than 0")
        self._tracks = tracks
        if not tracks:
            self._tracks = [{
                    "title": "Mirrors by Jason Richardson",
                    "link": "https://www.youtube.com/embed/Utj1VuJE7V0",
                },
                {
                    "title": "A Cruel Angel's Thesis",
                    "link": "https://www.youtube.com/embed/k8ozVkIkr-g",
                },
                {
                    "title": "505 by Arctic Monkeys",
                    "link": "https://www.youtube.com/embed/MrmPDUvKyLs",
                },
                {
                    "title": "More Than A Woman by The Bee Gees",
                    "link": "https://www.youtube.com/embed/zwyKQnbDJRg",
                },
                {
                    "title": "Billie Jean by Michael Jackson",
                    "link": "https://www.youtube.com/embed/Zi_XLOBDo_Y"
                }]

    def trackshuffle(self):
        random.shuffle(self._tracks)
        return self._tracks

class EshaanBubbleSort:
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
    def ConvertString(self,inarr):
        for j in range(0, len(inarr)):
            inarr[j] = inarr[j].upper()


    @property
    def OutputList(self):
        inarr = self.input_list
        if(self.isString):
            self.ConvertString(inarr)
            self.StringSort(inarr)
            for i in range(len(inarr)):
                self._output_list.append(inarr[i])
            return self._output_list
        else:
            self.bubblesort(inarr)
            for i in range(len(inarr)):
                self._output_list.append(inarr[i])
            return self._output_list