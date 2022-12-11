class Employee:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company

    def get_company(self):
        return self.company

    def set_company(self, company):
        self.company = company


class Boss(Employee):
    def __init__(self, id_: int, name: str, company: str):
        super().__init__(id_, name, company)

        self.workers = []

    def get_workers(self):
        return self.workers

    def set_workers(self, workers):
        self.workers = workers

    def add_worker(self, worker):
        worker.set_boss(self)
        worker.set_company(self.get_company())
        self.get_workers().append(worker)


class Worker(Employee):
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        super().__init__(id_, name, company)

        self.boss = boss
        self.boss.add_worker(self)

    def get_boss(self):
        return self.boss

    def set_boss(self, boss):
        self.company = boss.company
        self.boss = boss


microsoft_boss = Boss(1, "Bill", "Microsoft")
apple_boss = Boss(2, "Tim", "Apple")

assert microsoft_boss.get_workers() == []

workers = [
    Worker(1, "John", "Microsoft", microsoft_boss),
    Worker(2, "Bobby", "Microsoft", microsoft_boss),
]

assert microsoft_boss.get_workers() == workers

worker = Worker(3, "Sarah", "Microsoft", microsoft_boss)

microsoft_boss.add_worker(worker)

assert worker.get_company() == microsoft_boss.get_company()
assert worker.get_boss() == microsoft_boss
