#debt planner using OpenAI

from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key = config['API_KEY']

)

class DebtProfile:
    def __init__(self, first_name, debt_amount, monthly_expenses, annual_income, months_to_payoff):
        self.first_name = first_name
        self.debt_amount = debt_amount
        self.monthly_expenses = monthly_expenses
        self.annual_income = annual_income
        self.months_to_payoff = months_to_payoff
    
    def generate_plan(self):
        promp_message = (f"Write a debt payoff plan for {self.first_name} based on these attributes.\n" 
                      + f"Their current debt total is: ${self.debt_amount}"
                      + f"Their monthly expenses is: ${self.monthly_expenses}"
                      + f"Their annual income is: ${self.annual_income}"
                      + f"They expect to pay off their debt within {self.months_to_payoff} months"
                        )
        completion  = client.chat.completions.create(
            model = 'gpt-4',
            messages=[
                    {"role": "system", "content": "You are a financial advisor who creates realistic and supportive debt repayment plans."},
                    {"role": "user", "content": promp_message}
                    ],
            max_tokens = 600,
            temperature = 0.3
            )
        retreive_result = completion.choices[0].message.content.strip()
        print("\nGenerated Debt Plan:\n", retreive_result)


def get_debtor_input():
    first_name = input("Please provide your first name: ")
    debt_amount = input("Please provide your total debt: ")
    monthly_expenses = input("Please provide your total monthly expenses, this includes utilizes and essentials: ")
    annual_income = input("Please provide your annual income, after taxes: ")
    months_to_payoff = input("In how many months would you like to pay off all your debt? ")

    return DebtProfile(first_name, debt_amount, monthly_expenses, annual_income, months_to_payoff )


def main():
    details = get_debtor_input()
    details.generate_plan()

main()


