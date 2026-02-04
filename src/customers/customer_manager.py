class CustomerManager:
    def __init__(self, customers):
        self.customers = customers

    def display_customers(self):
        """Displays all customer records."""
        for cust_id, details in self.customers.items():
            print(f"ID: {cust_id} | Name: {details['name']} | Location: {details['location']} | Purchases: {details['purchases']}")

    def filter_customers_by_city(self, city):
        filtered_customers = {cust_id: details for cust_id, details in self.customers.items() if details["location"].lower() == city.lower()}
        if filtered_customers:
            print(f"\nCustomers in {city}")
        else:
            print(f"\nNo Customers found in {city}")

    def get_unique_locations(self):
        customer_locations = {customer["location"] for customer in self.customers.values()}
        print(customer_locations)
    
    def update_customer_location(self, customer_id, new_location):
        if customer_id in self.customers:
            old_location = self.customers[customer_id]["location"]
            self.customers[customer_id]["location"] = new_location
            print(f"\nUpdated {self.customers[customer_id]['name']}'s location from {old_location} to {new_location}.")
        else:
            print(f"\nCustomer not found")