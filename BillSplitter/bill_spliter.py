from collections import defaultdict

class BillSplitter:
    def __init__(self):
        self.balances = defaultdict(int)  # Պահում ենք՝ ով ում ինչքան է պարտք

    def add_expense(self, payer, amount, participants):
        """Ավելացնում է ծախս. payer-ը վճարել է amount գումարը, որը բաժանվում է participants-ի միջև"""
        if len(participants) == 0:
            print("Հաղորդագրություն. Սխալ մասնակիցներ")
            return
        share = amount / len(participants)
        for person in participants:
            if person != payer:
                self.balances[person] -= share  # Այս մարդը պետք է վճարի share գումարը
                self.balances[payer] += share   # Վճարողը ստանում է այդ գումարը
    
    def minimize_transactions(self):
        """Կատարում է նվազագույն փոխանցումներ՝ հնարավորինս կրճատելով գործարքների քանակը"""
        creditors = sorted([(p, b) for p, b in self.balances.items() if b > 0], key=lambda x: -x[1])
        debtors = sorted([(p, b) for p, b in self.balances.items() if b < 0], key=lambda x: x[1])
        
        transactions = []
        i, j = 0, 0
        
        while i < len(debtors) and j < len(creditors):
            debtor, debt = debtors[i]
            creditor, credit = creditors[j]
            
            # Մինիմալը փոխանցում ենք
            transfer_amount = min(-debt, credit)
            transactions.append((debtor, creditor, transfer_amount))
            
            # Մոդիֆիկացիա անել
            debtors[i] = (debtor, debt + transfer_amount)
            creditors[j] = (creditor, credit - transfer_amount)
            
            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1
        
        return transactions

    def print_balances(self):
        print("\n📊 Հաշվեկշիռներ (ով ում որքան է պարտք)")
        for person, balance in self.balances.items():
            print(f"{person}: {balance:.2f} AMD")
    
    def print_transactions(self):
        transactions = self.minimize_transactions()
        print("\n💰 Արդյունքում պետք է կատարվեն հետևյալ փոխանցումները՝")
        for debtor, creditor, amount in transactions:
            print(f"{debtor} → {creditor}: {amount:.2f} AMD")

# Օրինակ օգտագործում
splitter = BillSplitter()
splitter.add_expense("Արամ", 12000, ["Արամ", "Մարի", "Անի"])
splitter.add_expense("Մարի", 8000, ["Մարի", "Արամ"])
splitter.add_expense("Անի", 6000, ["Անի", "Մարի", "Արամ"])

splitter.print_balances()
splitter.print_transactions()
