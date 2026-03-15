CREATE TABLE records (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    category VARCHAR(50),
    merchant VARCHAR(100),
    description TEXT,
    amount NUMERIC(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO records (date, category, merchant, description, amount) VALUES
('2025-01-05', 'Food', 'McDonalds', 'Burger meal', 8.50),
('2025-01-07', 'Transport', 'Uber', 'Office ride', 12.00),
('2025-01-10', 'Shopping', 'Amazon', 'Headphones', 59.99),
('2025-01-12', 'Bills', 'Electricity Board', 'Electricity bill', 45.75),
('2025-01-15', 'Food', 'Dominos', 'Pizza order', 14.20),
('2025-01-18', 'Transport', 'Metro', 'Metro travel card', 10.00),
('2025-01-20', 'Shopping', 'Flipkart', 'Phone case', 7.99),
('2025-01-22', 'Entertainment', 'Netflix', 'Monthly subscription', 15.99),
('2025-01-25', 'Food', 'Starbucks', 'Coffee', 6.50),
('2025-01-28', 'Health', 'Pharmacy', 'Medicines', 18.40);