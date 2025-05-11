import os

ACCOUNT_FILE = "bank_accounts.txt"

def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, "r") as file:
            for line in file:
                acc_num, name, balance = line.strip().split(',')
                accounts[acc_num] = {"name": name, "balance": float(balance)}
    return accounts

def save_accounts(accounts):
    with open(ACCOUNT_FILE, "w") as file:
        for acc_num, info in accounts.items():
            file.write(f"{acc_num},{info['name']},{info['balance']}\n")

def create_account(accounts):
    acc_num = input("Enter new account number: ")
    if acc_num in accounts:
        print("Account already exists!")
        return
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial deposit amount: "))
    accounts[acc_num] = {"name": name, "balance": balance}
    save_accounts(accounts)
    print("Account created successfully.")

def deposit_amount(accounts):
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_num]["balance"] += amount
        save_accounts(accounts)
        print("Amount deposited successfully.")
    else:
        print("Account not found!")

def withdraw_amount(accounts):
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[acc_num]["balance"]:
            accounts[acc_num]["balance"] -= amount
            save_accounts(accounts)
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found!")

def balance_enquiry(accounts):
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        print(f"Account Holder: {accounts[acc_num]['name']}")
        print(f"Balance: {accounts[acc_num]['balance']}")
    else:
        print("Account not found!")

def all_accounts(accounts):
    print("\n--- All Account Holders ---")
    if not accounts:
        print("No accounts found.")
    for acc_num, info in accounts.items():
        print(f"Account No: {acc_num}, Name: {info['name']}, Balance: {info['balance']}")

def close_account(accounts):
    acc_num = input("Enter account number to close: ")
    if acc_num in accounts:
        del accounts[acc_num]
        save_accounts(accounts)
        print("Account closed successfully.")
    else:
        print("Account not found!")

def modify_account(accounts):
    acc_num = input("Enter account number to modify: ")
    if acc_num in accounts:
        print("1. Change Name")
        print("2. Change Balance")
        choice = input("Select what to modify: ")
        if choice == '1':
            new_name = input("Enter new name: ")
            accounts[acc_num]["name"] = new_name
        elif choice == '2':
            new_balance = float(input("Enter new balance: "))
            accounts[acc_num]["balance"] = new_balance
        else:
            print("Invalid choice.")
            return
        save_accounts(accounts)
        print("Account updated successfully.")
    else:
        print("Account not found!")

def main():
    accounts = load_accounts()
    while True:
        print("\n--- Bank Management System ---")
        print("1. New Account")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Balance Enquiry")
        print("5. All Account Holder List")
        print("6. Close An Account")
        print("7. Modify An Account")
        print("8. Exit")

        choice = input("Select Your Option (1-8): ")

        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit_amount(accounts)
        elif choice == '3':
            withdraw_amount(accounts)
        elif choice == '4':
            balance_enquiry(accounts)
        elif choice == '5':
            all_accounts(accounts)
        elif choice == '6':
            close_account(accounts)
        elif choice == '7':
            modify_account(accounts)
        elif choice == '8':
            print("Exiting the system. Thank you.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
