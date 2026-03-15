from db import db_connect



def total_expense(cursor):
    cursor.execute("SELECT SUM(amount) FROM records;")
    total = cursor.fetchone()[0]
    return total

def average_expense(cursor):
    cursor.execute("SELECT ROUND(AVG(amount),2) FROM records;")
    total = cursor.fetchone()[0]
    return total
    
def expense_category(cursor):
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM records
    GROUP BY category
    ORDER BY SUM(amount) DESC
    """)
    results = cursor.fetchall()
    return results


    
def top_expenses(cursor):
    cursor.execute("""
    SELECT merchant, amount
    FROM records
    ORDER BY amount DESC
    LIMIT 5
    """)
    results = cursor.fetchall()
    return results

def monthly_expense(cursor):
    cursor.execute(""" SELECT DATE_TRUNC('month', date) AS month, SUM(amount)
    FROM records
    GROUP BY month
    ORDER BY month
    """)
    results = cursor.fetchall()
    return results
    
    


def run_analytics():

    conn, cursor = db_connect()

    print("\nRunning Expense Analytics...")
    print("--------------------------------\n")

    # TOTAL EXPENSE
    total = total_expense(cursor)
    print("Total Expense:")
    print(total)
    print()

    # AVERAGE EXPENSE
    avg = average_expense(cursor)
    print("Average Expense:")
    print(avg)
    print()

    # # EXPENSE BY CATEGORY
    
    print("Expense by Category:")
    print("--------------------------------")
    cat_data = expense_category(cursor)
    print(f"{'Category':<15}{'Total'}")

    for row in cat_data:
        print(f"{row[0]:<15}{row[1]}")
    print()

    # TOP 5 EXPENSES
    print("Top 5 Expenses:")
    print("--------------------------------")
    expense_data = top_expenses(cursor)
    print(f"{'Merchant':<20}{'Amount'}")

    for row in expense_data:
        print(f"{row[0]:<20}{row[1]}")
    print()

    # # MONTHLY EXPENSE
    print("Monthly Expense:")
    print("--------------------------------")
    monthly_data = monthly_expense(cursor)
    print(f"{'Month':<15}{'Total'}")

    for row in monthly_data:
        month = row[0].strftime("%Y-%m")
        print(f"{month:<15}{row[1]}")

    print("\nAnalytics completed successfully")

    cursor.close()
    conn.close()