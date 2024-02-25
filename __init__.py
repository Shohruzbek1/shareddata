class SharedData:
    """SharedData v1.3 by Shohruzbek, description: used to save data on computer memory"""
    """
    Changelog:
        v1.0:
            module released
        v1.1:
            added append(data), update data without losing old data
        v1.2:
            added last read feature for use cached last data when getting data from memory, useful for use data.get() multiple times, reduce lag and optimize code
        v1.3:
            added clear method to clear data from memory
            fixed bugs
    """
    
    def __init__(self,filename = "data.txt"):
        """"Create new SharedData element if need use filename = 'file.txt'"""
        self.lastRead = ""
        self.filename = filename
        try:
            open(self.filename,"r").close()
        except:
            self.cache = open(self.filename,"w")
            self.cache.write("")
            self.cache.close()

    def get(self):
        """Get data from memory"""
        if self.lastRead:
            return self.lastRead
        else:
            self.dataRead = self.datafile = open(self.filename,"r")
            self.data = self.dataRead.read()
            self.dataRead.close()
            self.lastRead = self.data
            return self.data

    def update(self,data):
        """Update data, use data.append() if you don't want to lose last saved data"""
        self.dataWrite = open(self.filename,"w")
        self.dataWrite.write(str(data))
        self.dataWrite.close()
        self.lastRead = ""
    
    def append(self,data):
        """Append data to the last data"""
        self.dataAppend = open(self.filename,"a")
        self.dataAppend.write(str(data))
        self.dataAppend.close()
        self.lastRead = ""

    def clear(self):
        """Clear data from memory"""
        self.update("")
