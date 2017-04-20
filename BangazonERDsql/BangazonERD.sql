CREATE TABLE Department (
	DepartmentID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Title TEXT NOT NULL,
	Expense_Budget INTEGER NOT NULL,
	SupervisorID INTEGER NOT NULL
);

SELECT FROM Department;
INSERT INTO Department VALUES (null, "HR", 1000, 12345)



CREATE TABLE Employee (
	EmployeeID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Title TEXT NOT NULL,
	First_Name TEXT NOT NULL,
	Last_Name TEXT NOT NULL,
	DepartmentID INTEGER NOT NULL,
	FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);
	
	CREATE TABLE TrainingProgram(
	TrainingProgramID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Start_Date INTEGER NOT NULL,
	End_Date INTEGER NOT NULL,
	Maximum_Attendees INTEGER NOT NULL,
	Program_Title TEXT NOT NULL
);

CREATE TABLE EmployeeTrainingProgram(
	EmployeeTrainingProgramID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	TrainingProgramID INTEGER NOT NULL,
	EmployeeID INTEGER NOT NULL,
	FOREIGN KEY (TrainingProgramID) REFERENCES TrainingProgram(TrainingProgramID),
	FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID )
);

CREATE TABLE Computer(
	ComputerID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Purchase_Date INTEGER NOT NULL,
	Decommission_Date INTEGER NOT NULL,
	Type TEXT NOT NULL
);

CREATE TABLE EmployeeComputer(
	EmployeeComputerID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	EmployeeID INTEGER NOT NULL,
	ComputerID INTEGER NOT NULL,
	FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
	FOREIGN KEY (ComputerID) REFERENCES Computer(ComputerID)
);


CREATE TABLE ProductType(
	ProductTypeID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Category_Name TEXT NOT NULL
	);
	
CREATE TABLE Customer(
	CustomerID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	First_Name TEXT NOT NULL,
	Last_Name TEXT NOT NULL,
	Date_Acct_Created INTEGER NOT NULL,
	Active INTEGER NOT NULL
	/**Active field 0=FALSE, 1=TRUE **/
);


CREATE TABLE Product(
	ProductD INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Price INTEGER NOT NULL,
	Title TEXT NOT NULL,
	Description TEXT NOT NULL,
	ProductTypeID INTEGER NOT NULL,
	CustomerID INTEGER NOT NULL,
	FOREIGN KEY (ProductTypeID) REFERENCES ProductType(ProductTypeID),
	FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

Create TABLE OrderTable(
	OrderID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	PaymentTypeID INTEGER NOT NULL,
	Paid INTEGER NOT NULL
	/**Paid field 0=FALSE, 1=TRUE **/
);

Create TABLE PaymentType(
	PaymentTypeID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Account_Number INTEGER NOT NULL,
	CustomerID INTEGER NOT NULL,
	FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);


CREATE TABLE ProductOrder(
	ProductOrderID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	ProductID INTEGER NOT NULL,
	OrderID INTEGER NOT NULL,
	FOREIGN KEY (ProductID) REFERENCES ProductI(ProductID),
	FOREIGN KEY (OrderID) REFERENCES OrderTable(OrderID)
);




DROP TABLE IF EXISTS Product_Type
DROP TABLE IF EXISTS Product
DROP TABLE IF EXISTS Department
DROP TABLE IF EXISTS Training_Program
DROP TABLE IF EXISTS TrainingProgram
DROP TABLE IF EXISTS Employee_Training_Program