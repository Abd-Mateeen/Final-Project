USE restaurant_reservation; 
CREATE TABLE Customers (
customerId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
customerName VARCHAR(45) NOT NULL,
contactInfo VARCHAR(200) 
);
 INSERT INTO Customers (customerName, contactInfo)
 VALUES( "NANCY KIND",  "347-889-0909"),( "JAMES ANDERSON","2890-712-35678"), ( "MALIK MOUSE", "322-567-9087"); 
 SELECT * FROM customers;
 CREATE TABLE Reservations (
 reservationId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
 customerId INT NOT NULL,
 reservationTime DATETIME NOT NULL,
 numberOfGuests INT NOT NULL,
 specialRequests VARCHAR(200),    
 FOREIGN KEY (customerId) REFERENCES Customers(customerId) 
 ); 
 
 SELECT * FROM reservations; 
 CREATE TABLE DiningPreferences (
 preferenceId INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
 customerId INT NOT NULL,  
 favoriteTable VARCHAR(45),
 dietaryRestrictions VARCHAR(200), 
 FOREIGN KEY (customerId) REFERENCES Customers(customerId) 
 ); 
 
 SELECT * FROM DiningPreferences;
