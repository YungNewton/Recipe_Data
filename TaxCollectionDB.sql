
CREATE TABLE Individuals (
    DocumentNumber VARCHAR(20) PRIMARY KEY,
    FullName VARCHAR(100),
    DateOfBirth DATE,
    HomeAddress VARCHAR(255),
    Email VARCHAR(100),
    Landline VARCHAR(15),
    Mobile VARCHAR(15),
    Fax VARCHAR(15)
);

CREATE TABLE Companies (
    CUIT VARCHAR(20) PRIMARY KEY,
    CommencementDate DATE,
    Website VARCHAR(255),
    Email VARCHAR(100),
    Landline VARCHAR(15),
    Mobile VARCHAR(15),
    Fax VARCHAR(15)
);

CREATE TABLE Agency (
    OfficeNumber INT PRIMARY KEY,
    Address VARCHAR(255),
    Telephone VARCHAR(15),
    PersonInCharge VARCHAR(50),
    
 