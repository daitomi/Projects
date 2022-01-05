import math
import argparse

checks = True

# parser creation
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"],
                    help="please type either \"annuity\" or \"diff\" ")

parser.add_argument("--payment", type=int,
                    help="monthly payment amount")
parser.add_argument("--principal", type=int,
                    help="is used for calculations of both types of payment")
parser.add_argument("--periods", type=int,
                    help="denotes the number of months needed to repay the loan")
parser.add_argument("--interest", type=float,
                    help="specified without a percent sign")

args = parser.parse_args()


# a list for the negative number error
alist = []

for arg in vars(args):
    if getattr(args, arg) is not None:
        alist.append(getattr(args, arg))

smol = min(alist[1:4])


# incorrect parameter errors

if args.type not in ("diff", "annuity"):
    print('Incorrect parameters')
    checks = False

elif args.type == "diff" and args.payment is not None:
    print('Incorrect parameters')
    checks = False

elif args.interest is None or args.type is None:
    print('Incorrect parameters')
    checks = False

# error: number negative
elif args.interest < 0:
    print('Incorrect parameters')
    checks = False

elif smol < 0:
    print('Incorrect parameters')
    checks = False

# error: not enough parameters
elif len(alist) != 4:
    print('Incorrect parameters')
    checks = False


# calculations

if checks:

    nominal_interest = (1 / 12) * (args.interest / 100)

    if args.type == "diff":

        m = 1
        diff_list = []

        limit = args.periods + 1
        months = list(range(1, limit))

        for m in months:
            sub = ((args.principal * (m - 1)) / args.periods)
            Diff_pay = args.principal / args.periods + nominal_interest * (args.principal - sub)

            diff_list.append(math.ceil(Diff_pay))

            print(f"Month {m}: payment is {math.ceil(Diff_pay)}")
            m += 1

        overpayment = sum(diff_list) - args.principal
        print(f"\nOverpayment = {overpayment}")


    elif args.principal is None:
        side_1 = (nominal_interest * pow((1 + nominal_interest), args.periods))
        side_2 = (pow((1 + nominal_interest), args.periods) - 1)

        loan_principal = args.payment / (side_1 / side_2)

        print(f"Your loan principal = {round(loan_principal)}!")

        overpayment = (args.payment * args.periods) - round(loan_principal)
        print(f"Overpayment = {int(overpayment)}")


    elif args.periods is None:

        x = (args.payment / (args.payment - nominal_interest * args.principal))
        base = (1 + nominal_interest)
        n = math.ceil(math.log(x, base))
        year_num = int(n // 12)
        months_num = math.ceil(n - (year_num * 12))

        year = "years"
        month = "months"

        if year_num == 1:
            year = "year"

        if months_num == 1:
            month = "month"

        if year_num == 0:
            print(f"It will take {months_num} {month} to repay this loan!")

        elif months_num == 0:
            print(f"It will take {year_num} {year} to repay this loan!")

        else:
            print(f"It will take {year_num} {year} and {months_num} {month} to repay this loan!")

        overpayment = (n * args.payment) - args.principal

        print(f"Overpayment = {int(overpayment)}")


    elif args.payment is None:
        side_1 = (nominal_interest * pow((1 + nominal_interest), args.periods))
        side_2 = (pow((1 + nominal_interest), args.periods) - 1)

        annuity_pay = math.ceil(args.principal * (side_1 / side_2))

        print(f"Your annuity payment = {annuity_pay}!")

        overpayment = (annuity_pay * args.periods) - args.principal

        print(f"Overpayment = {overpayment}")

