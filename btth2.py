atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balances():

    global user_account_balance
    global atm_vault_balance

    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    global user_account_balance
    global atm_vault_balance

    user_account_balance += amount
    atm_vault_balance += amount

    return True


def check_withdrawal_rules(amount):

    global user_account_balance
    global atm_vault_balance

    fee = 1100

    if amount <= 0:
        return "INVALID_AMOUNT", 0

    if amount % 50000 != 0:
        return "INVALID_MULTIPLE", 0

    total_deduction = amount + fee

    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS", 0

    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH", 0

    return "OK", total_deduction


def execute_withdrawal(total_deduction, amount_to_dispense):

    global user_account_balance
    global atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense

    print("\nGiao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(
        f"Số dư tài khoản còn lại: "
        f"{user_account_balance:,} VND."
    )


def main():

    while True:

        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")

        choice = input("Vui lòng chọn giao dịch (1-4): ")

        match choice:

            case "1":
                display_balances()

            case "2":
                print("\n--- NẠP TIỀN ---")

                try:
                    amount = int(
                        input("Nhập số tiền muốn nạp: ")
                    )

                    if amount <= 0:
                        print("Số tiền không hợp lệ")
                        continue

                    if deposit_money(amount):
                        print(
                            f"Giao dịch thành công! "
                            f"Số dư tài khoản hiện tại: "
                            f"{user_account_balance:,} VND."
                        )

                except ValueError:
                    print("Vui lòng nhập đúng định dạng số.")

            case "3":
                print("\n--- RÚT TIỀN ---")

                try:
                    amount = int(
                        input("Nhập số tiền cần rút: ")
                    )

                    status, total_deduction = (
                        check_withdrawal_rules(amount)
                    )

                    match status:

                        case "INVALID_AMOUNT":
                            print("Số tiền không hợp lệ")

                        case "INVALID_MULTIPLE":
                            print(
                                "Số tiền rút phải là bội số của 50,000"
                            )

                        case "INSUFFICIENT_FUNDS":
                            print(
                                "Giao dịch thất bại: "
                                "Tài khoản không đủ số dư."
                            )

                        case "ATM_OUT_OF_CASH":
                            print(
                                "Giao dịch thất bại: "
                                "Máy ATM không đủ tiền mặt để phục vụ."
                            )

                        case "OK":
                            execute_withdrawal(
                                total_deduction,
                                amount
                            )

                except ValueError:
                    print("Vui lòng nhập đúng định dạng số.")

            case "4":
                print(
                    "\nCảm ơn quý khách đã sử dụng dịch vụ!"
                )
                break

            case _:
                print("Lựa chọn không hợp lệ.")


main()