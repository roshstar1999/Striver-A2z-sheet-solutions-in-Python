
class AutoCompleteSystem():
    def __init__(self, sentences, times):
        # write code for constructor
        self.hist={}
        for i in range(len(sentences)):
            self.hist[sentences[i]]=times[i]
        self.prefix=''
    
    def input(self,c):
        '''
        
            write code to return the top 3 suggestions when the current character in the stream is c
            c == '#' means , the current query is complete and you may save the entire query into
            historical data
        '''
        if c=='#':
            if self.prefix not in self.hist:
                self.hist[self.prefix]=0
            self.hist[self.prefix]+=1
            self.prefix=''
            return
        
        self.prefix+=c
        matches=[s for s in self.hist if s.startswith(self.prefix)]
        matches.sort(key=lambda x: (-self.hist[x],x) )
        return matches[:3]
