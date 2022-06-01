import datetime
import os
from sqlite3 import DataError
import csv

file_location = os.path.dirname(__file__)
risk_assessments_folder = os.path.join(file_location, "Risk Assessments")
file_location_risks_folder = os.path.join(file_location, "Risks")
templates_folder = os.path.join(file_location, "Template")
budgets_location = os.path.join(file_location, "Budgets")


def run():

    os.chdir(file_location)
    if not os.path.exists("Budgets"):
        """Creates a sub-directory called "Budgets" within the directory of this __file__
        Budgets that are created by the user will be stored here as CSV files
        """
        print(f"Creating directory 'Budgets' in {file_location}")
        os.makedirs("Budgets")

    class Element:
        """Class for instantiating outgoing costs."""

        def __init__(
            self,
            name: str,
            amount: int,
            outgoing_date: int,
            payment_method: str,
            renewal_date: str,
            essential: str,
            frequent: str,
            typof: str,
        ):
            params = [
                "Bank Transfer",
                "Card",
                "Cash",
                "Paye",
                "BACS",
                "Direct Debit",
                "Other",
            ]
            self.name = name
            self.amount = amount
            self.outgoing_date = outgoing_date
            self.payment_method = payment_method
            self.renewal_date = renewal_date
            self.essential = essential
            self.frequent = frequent
            self.typof = typof

            validate_date(self.renewal_date)

            if self.payment_method.title() in params:
                """User validation to require user to only input
                strings found in 'params'
                """
                pass
            else:
                raise TypeError(
                    "Only 'Bank Transfer', 'Card', 'Cash' or 'Other' can be accepted"
                )

            types = ["Expense", "Saving", "Income"]

            if self.typof.title() in types:
                """User validation to require user to only input
                strings found in 'types'
                """
                pass
            else:
                raise TypeError(
                    "Only 'Expense', 'Saving', or 'Income', can be accepted"
                )

        def monthly_amount(self):
            """Returns the ammount needed to be put
            aside each month to cover the annual cost.
            """
            return f"Monthly cost: £{round(self.amount / 12, 2):,}"

        def annual_cost(self):
            """Returns the total cost of the expense
            over 12 months.
            """
            return self.amount

    def validate_date(date_text):
        """User validation for desired date format:
        DD/MM/YYY
        """
        if date_text == "N/A":
            pass
        else:
            try:
                datetime.datetime.strptime(date_text, "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                raise ValueError("Date must be formatted as DD-MM-YYYY")

    def add_element(
        name: str,
        amount: int,
        outgoing_date: int,
        payment_method: str,
        renewal_date: str,
        essential: str,
        frequent: str,
        typof: str,
    ):
        """Create an instance of the Outgoing() class.
        Requires seven paramaters:
        name:str, amount:int, outgoing_date: str,
        payment_method: str, renewal_date: str, essential: str,
        frequent: user validation converts to bool

        Validates user input to convert frequent into
        bool.

        Throws error if desired input for frequent
        is not provided.
        """

        days = range(0, 32)
        if outgoing_date in days:
            validate_date(renewal_date)
            if (
                frequent.title() == "Yes"
                or frequent.title() == "Y"
                or frequent.title() == "No"
                or frequent.title() == "N"
            ):
                if frequent.title() == "Yes" or frequent.title() == "Y":
                    frequent = True
                elif frequent.title() == "No" or frequent.title() == "N":
                    frequent = False
            else:
                raise DataError("Incorrect input provided. Must be (Yes/No) or (Y/N)")

            if essential == "N/A":
                pass
            else:
                if (
                    essential.title() == "Yes"
                    or essential.title() == "Y"
                    or essential.title() == "No"
                    or essential.title() == "N"
                ):
                    if essential.title() == "Yes" or essential.title() == "Y":
                        essential = True
                    elif essential.title() == "No" or essential.title() == "N":
                        essential = False
                else:
                    raise DataError(
                        "Incorrect input provided. Must be (Yes/No) or (Y/N)"
                    )

            name = Element(
                name,
                amount,
                outgoing_date,
                payment_method,
                renewal_date,
                essential,
                frequent,
                typof,
            )

            os.chdir(os.path.join(file_location, "Budgets"))
            if not os.path.exists(os.path.join(budgets_location, "Budget.csv")):

                with open("Budget.csv", "w", newline="") as budget:
                    writer = csv.writer(budget)
                    print("Creating new CSV file")
                    writer.writerow(
                        [
                            "Item",
                            "Amount",
                            "Outgoing Date",
                            "Renewal Date",
                            "Essential",
                            "Payment Method",
                            "Payment Frequency",
                            "Type",
                        ]
                    )
                    writer.writerow(
                        [
                            f"{name.name}",
                            f"{amount}",
                            f"{outgoing_date}",
                            f"{renewal_date}",
                            f"{essential}",
                            f"{payment_method}",
                            f"{frequent}",
                            f"{typof}",
                        ]
                    )
                    budget.close()

            elif os.path.exists(
                os.path.join(os.path.join(budgets_location, "Budget.csv"))
            ):
                with open(
                    os.path.join(budgets_location, "Budget.csv"),
                    "r+",
                    newline="",
                ) as budget:
                    budget_reader = csv.reader(budget)
                    row_name = []
                    for row in budget_reader:
                        """Creates a list of all the current named expenses"""
                        row_name.append(row[0])

                    if name.name in row_name:
                        """Searches the list for matching input and exits if
                        a match exists
                        """
                        print(f"{name.name} is already present")
                    else:
                        writer = csv.writer(budget)
                        writer.writerow(
                            [
                                f"{name.name}",
                                f"{amount}",
                                f"{outgoing_date}",
                                f"{renewal_date}",
                                f"{essential}",
                                f"{payment_method}",
                                f"{frequent}",
                                f"{typof}",
                            ]
                        )
                        print(f"Item: {name.name}")
                        print(f"Amount: £{amount:,}")
                        print(f"Outgoing day of month: {name.outgoing_date}")
                        print(f"Payment method: {name.payment_method}")
                        print(f"Renewal date: {name.renewal_date}")
                        print(f"Essential: {name.essential}")
                        print(f"Regular expense: {name.frequent}")
                        print(f"Type: {typof}")
                        print("")
                    budget.close()
        else:
            print(f"Outgoing date must be between 0-31")

    def calculate_expense():
        expense_sum = 0
        with open(os.path.join(budgets_location, "Budget.csv")) as f:
            reader = csv.reader(f)
            try:
                for index, row in enumerate(list(reader)[1:]):
                    if row[7] == "Expense":
                        expense_sum += float(row[1])
                    else:
                        continue

                print(f"Total monthly expense: £{round(expense_sum,2):,.2f}")
            except:
                pass
            f.close()

    def list_expenses():
        expenses = []
        with open(os.path.join(budgets_location, "Budget.csv"), "r") as le:
            le_reader = csv.reader(le)
            for le_row in le_reader:
                if le_row[7] == "Expense":
                    expenses.append(le_row[0])
                else:
                    continue
            print(expenses)

    def calculate_saving():
        saving_sum = 0
        with open(os.path.join(budgets_location, "Budget.csv")) as f:
            reader = csv.reader(f)
            try:
                for index, row in enumerate(list(reader)[1:]):
                    if row[7] == "Saving":
                        saving_sum += float(row[1])
                    else:
                        continue

                print(f"Total monthly saving: £{round(saving_sum,2):,.2f}")
            except:
                pass
            f.close()

    def list_savings():
        savings = []
        with open(os.path.join(budgets_location, "Budget.csv"), "r") as ls:
            ls_reader = csv.reader(ls)
            for ls_row in ls_reader:
                if ls_row[7] == "Saving":
                    savings.append(ls_row[0])
                else:
                    continue
            print(savings)

    def calculate_income():
        income_sum = 0
        with open(os.path.join(budgets_location, "Budget.csv")) as f:
            reader = csv.reader(f)
            try:
                for index, row in enumerate(list(reader)[1:]):
                    if row[7] == "Income":
                        income_sum += float(row[1])
                    else:
                        continue

                print(f"Total monthly income £{round(income_sum,2):,.2f}")
            except:
                pass
            f.close()

    def list_incomes():
        incomes = []
        with open(os.path.join(budgets_location, "Budget.csv"), "r") as li:
            li_reader = csv.reader(li)
            for li_row in li_reader:
                if li_row[7] == "Income":
                    incomes.append(li_row[0])
                else:
                    continue
            print(incomes)

    def list_payment_types():
        request_type = input("What do you want to search for?\n")
        payment_types = []
        with open(os.path.join(budgets_location, "Budget.csv"), "r") as pt:
            pt_reader = csv.reader(pt)
            for pt_row in pt_reader:
                if pt_row[5] == request_type.title():
                    payment_types.append(pt_row[0])
                else:
                    continue
            if payment_types == []:
                print("Payment type was not found.")
            else:
                print(payment_types)

    def remove_element(param):
        lines = []
        with open(
            os.path.join(os.path.join(budgets_location, "Budget.csv"), "r+", newline="")
        ) as read_file:
            reader = csv.reader(read_file)
            writer = csv.writer(read_file)

            for i, r in enumerate(list(reader)):

                if r[0] == param:
                    print(f"Yes: {r[0]}")
                elif not r[0] == param:
                    print(f"No: {r[0]}")
                    lines.append(r)
            read_file.seek(0)
            read_file.truncate()
            writer.writerows(lines)
            read_file.close()

    def add_new_item():
        rp = [
            "Name - (Text)",
            "Amount - (Number)",
            "Outgoing Date - (1-31)",
            "Payment Method - ('Bank Transfer', 'Card', 'Cash', 'Paye', 'BACS', 'Direct Debit', 'Other')",
            "Renewal Date - (DD/MM/YYY) or ('Yes'/'No') or ('N/A')",
            "Essential - ('Yes'/'No') or ('N/A')",
            "Occurs monthly - ('Yes'/'No') or ('N/A')",
            "Type - ('Expense'/'Saving'/'Income')",
        ]
        for i, v in enumerate(rp):
            rp[i] = input(f"Enter new {v}:\n")
        add_element(rp[0], int(rp[1]), int(rp[2]), rp[3], rp[4], rp[5], rp[6], rp[7])

    """add_element("Gifts", 45, 30, "Bank Transfer", "N/A", "Yes", "Yes", "Expense")
    add_element("Household", 20, 30, "Bank Transfer", "N/A", "Yes", "Yes", "Expense")
    add_element("Wage", 1600, 31, "Bank Transfer", "N/A", "Yes", "Yes", "Income")
    add_element("Saving", 400, 1, "Bank Transfer", "N/A", "Yes", "Yes", "Saving")
    calculate_expense()
    calculate_income()
    calculate_saving()
    list_expenses()
    list_incomes()
    list_savings()
    list_payment_types()
    add_new_item()
    remove_element(param)
    """
    # add_new_item()
    list_expenses()
    calculate_expense()


if __name__ == "__main__":
    run()
