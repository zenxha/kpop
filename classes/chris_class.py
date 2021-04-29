import random

class song:
    def __init__(self):
            self._songs = [{
                                "title": "Party Rock Anthem",
                                "link": "https://www.youtube.com/embed/KQ6zr6kCPj8",
                            },
                            {
                                "title": "Uptown Funk",
                                "link": "https://www.youtube.com/embed/OPf0YbXqDm0",
                            },
                            {
                                "title": "Wrecking Ball",
                                "link": "https://www.youtube.com/embed/My2FRPA3Gf8",
                            },
                            {
                                "title": "A Thousand Miles",
                                "link": "https://www.youtube.com/embed/Cwkej79U3ek",
                            }]

    def songshuffle(self):
        random.shuffle(self._songs)
        return self._songs



class BubbleSort:
    def __init__(self, input_list,isString):
        self.input_list = input_list
        self._output_list = []
        self.bubblesort(input_list)
        self.isString = isString

    def bubblesort(self, inarr):
        n = len(inarr)
        for i in range(n):
            for j in range(0, n-i-1):
                if inarr[j] > inarr[j+1] :
                    inarr[j], inarr[j+1] = inarr[j+1], inarr[j]
    def StringSort(self, inarr):
        string = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'j', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X',
                 'Y','Z']
        for j in range(0, len(inarr)):
            for i in range(0, len(inarr)):
                _sorted = False
                if i != len(inarr)-1:
                    for k in range(0,len(inarr[i])):
                        if not _sorted:
                            if k != (len(inarr[i]) and len(inarr[i+1])):
                                if string.index(inarr[i][k]) > string.index(inarr[i+1][k]):
                                    inarr[i], inarr[i+1] = inarr[i+1], inarr[i]
                                    _sorted = True
                                elif string.index(inarr[i][k]) < string.index(inarr[i+1][k]):
                                    _sorted = True
                                else:
                                    if len(inarr[i+1]) < len(inarr[i]):
                                        inarr[i], inarr[i+1] = inarr[i+1], inarr[i]
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