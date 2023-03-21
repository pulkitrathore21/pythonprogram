class Task:
    def __init__(self,taskid,taskname,taskdescrip,taskpriority):
        self.taskid=taskid
        self.taskname=taskname
        self.taskdescrip=taskdescrip
        self.taskpriority=taskpriority

    def __str__(self):
        return f"({self.taskid}{self.taskname},{self.taskdescrip},{self.taskpriority})"
