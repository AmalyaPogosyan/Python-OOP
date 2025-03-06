import streamlit as st
from collections import defaultdict

class BillSplitter:
    def __init__(self):
        self.balances = defaultdict(int)

    def add_expense(self, payer, amount, participants):
        if not participants:
            st.warning("Պետք է նշել մասնակիցներին։")
            return
        share = amount / len(participants)
        for person in participants:
            if person != payer:
                self.balances[person] -= share
                self.balances[payer] += share
    
    def minimize_transactions(self):
        creditors = sorted([(creditor, balance) for creditor, balance in self.balances.items() if balance > 0], key=lambda x: -x[1])
        debtors = sorted([(debtor, balance) for debtor, balance in self.balances.items() if balance < 0], key=lambda x: x[1])
        transactions = []
        i, j = 0, 0

        while len(creditors) != 0:
            debtor, debt = debtors[0]
            creditor, credit = creditors[0]

            transfer_amount = min(-debt, credit)
            transactions.append((debtor, creditor, transfer_amount))

            self.balances[debtor] += transfer_amount
            self.balances[creditor] -= transfer_amount

            creditors = sorted([(p, b) for p, b in self.balances.items() if b > 0], key=lambda x: -x[1])
            debtors = sorted([(p, b) for p, b in self.balances.items() if b < 0], key=lambda x: x[1])
        return transactions


    def get_balances(self):
        return self.balances

st.title("💰 Bill Splitter")
st.write("Հաշիվների բաշխման համակարգ")

if "expenses" not in st.session_state:
    st.session_state["expenses"] = []

payer = st.text_input("Վճարող:")
amount = st.number_input("Գումար:", min_value=0.0, format="%.2f")
participants = st.text_area("Մասնակիցներ (բաժանեք ստորակետով):").split(",")
participants = [p.strip() for p in participants if p.strip()]

if st.button("Ավելացնել ծախս"):
    if payer and amount > 0 and participants:
        st.session_state["expenses"].append((payer, amount, participants))
        st.success("Ծախսը հաջողությամբ ավելացվեց")
    else:
        st.error("Խնդրում ենք լրացնել բոլոր տվյալները")

if st.button("Հաշվել պարտքերը"):
    splitter = BillSplitter()
    for payer, amount, participants in st.session_state["expenses"]:
        splitter.add_expense(payer, amount, participants)
    
    st.subheader("📊 Հաշվեկշիռներ")
    balances = splitter.get_balances()
    for person, balance in balances.items():
        st.write(f"{person}: {balance:.2f} AMD")
    
    st.subheader("💰 Նվազագույն փոխանցումներ")
    transactions = splitter.minimize_transactions()
    for debtor, creditor, amount in transactions:
        st.write(f"{debtor} → {creditor}: {amount:.2f} AMD")
