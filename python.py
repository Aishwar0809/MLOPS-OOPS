class employee:
    def __init__(self):
        self.id=111
        self.salary=50000
        self.designation="SDE"
    def travel(self,destination):
        print(f"sam is travelling to {destination}")

sam = employee()

print(sam.id)
sam.travel("Lucknow")