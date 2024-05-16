import mysql.connector

class RestaurantDatabase:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host='localhost',
            port='3306',
            database='restaurant_reservation',
            user='root',
            password='Abdul339832!')
            
        self.cursor = self.connection.cursor()

    def addReservation(self, customerName, reservationTime, numberOfGuests, specialRequests):
        try:
            # Check if customer exists
            self.cursor.execute("SELECT customerId FROM Customers WHERE customerName = %s", (customerName,))
            customer = self.cursor.fetchone()

            if customer:
                customerId = customer[0]
            else:
                # If the customer doesn't exist, add them
                self.cursor.execute("INSERT INTO Customers (customerName) VALUES (%s)", (customerName,))
                customerId = self.cursor.lastrowid

            # Add reservation
            self.cursor.execute("INSERT INTO Reservations (customerId, reservationTime, numberOfGuests, specialRequests) VALUES (%s, %s, %s, %s)",
                                (customerId, reservationTime, numberOfGuests, specialRequests))
            self.connection.commit()
            print("Reservation added successfully.")
        except mysql.connector.Error as error:
            print("Failed to add reservation:", error)

    def updateReservation(self, reservationId, specialRequests):
        try:
            # Update special requests for the reservation
            self.cursor.execute("UPDATE Reservations SET specialRequests = %s WHERE reservationId = %s", (specialRequests, reservationId))
            self.connection.commit()
            print("Reservation updated successfully.")
        except mysql.connector.Error as error:
            print("Failed to update reservation:", error)

    def deleteReservation(self, reservationId):
        try:
            # Delete reservation
            self.cursor.execute("DELETE FROM Reservations WHERE reservationId = %s", (reservationId,))
            self.connection.commit()
            print("Reservation deleted successfully.")
        except mysql.connector.Error as error:
            print("Failed to delete reservation:", error)

    def addDiningPreference(self, customerName, favoriteTable, dietaryRestrictions):
        try:
            # Check if customer exists
            self.cursor.execute("SELECT customerId FROM Customers WHERE customerName = %s", (customerName,))
            customer = self.cursor.fetchone()

            if customer:
                customerId = customer[0]
            else:
                # If the customer doesn't exist, add them
                self.cursor.execute("INSERT INTO Customers (customerName) VALUES (%s)", (customerName,))
                customerId = self.cursor.lastrowid

            # Add dining preference
            self.cursor.execute("INSERT INTO DiningPreferences (customerId, favoriteTable, dietaryRestrictions) VALUES (%s, %s, %s)",
                                (customerId, favoriteTable, dietaryRestrictions))
            self.connection.commit()
            print("Dining preference added successfully.")
        except mysql.connector.Error as error:
            print("Failed to add dining preference:", error)

    def __del__(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection closed.")

def main():
    # MySQL Connection details
    host = 'localhost'
    port= '3306'
    user = 'root'
    password = 'Abdul339832!'
    database = 'restaurant_reservations'

    # Connect to MySQL database
    db = RestaurantDatabase(host, user, password, database)

    while True:
        print("\n1. Add Reservation")
        print("2. Update Reservation")
        print("3. Delete Reservation")
        print("4. Add Dining Preference")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Get reservation details from user input
            customerName = input("Enter customer name: ")
            reservationTime = input("Enter reservation time (YYYY-MM-DD HH:MM:SS): ")
            numberOfGuests = int(input("Enter number of guests: "))
            specialRequests = input("Enter special requests: ")
            # Add reservation to database
            db.addReservation(customerName, reservationTime, numberOfGuests, specialRequests)
        elif choice == '2':
            # Get reservation ID and updated special requests from user input
            reservationId = int(input("Enter reservation ID to update: "))
            specialRequests = input("Enter updated special requests: ")
            # Update reservation in database
            db.updateReservation(reservationId, specialRequests)
        elif choice == '3':
            # Get reservation ID from user input
            reservationId = int(input("Enter reservation ID to delete: "))
            # Delete reservation from database
            db.deleteReservation(reservationId)
        elif choice == '4':
            # Get dining preference details from user input
            customerName = input("Enter customer name: ")
            favoriteTable = input("Enter favorite table: ")
            dietaryRestrictions = input("Enter dietary restrictions: ")
            # Add dining preference to database
            db.addDiningPreference(customerName, favoriteTable, dietaryRestrictions)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
