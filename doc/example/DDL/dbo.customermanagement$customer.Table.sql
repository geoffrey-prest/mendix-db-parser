USE [OnlineBookStore];

/**** Lorem ipsum dolor 234 #$% ****/

CREATE TABLE [dbo].[customermanagement$customer] (
    [id] [int] PRIMARY KEY,
    [name] [varchar](100) NOT NULL,
    [email] [varchar](100) UNIQUE,
    [passwordhash] [varchar](255) NOT NULL,
    [address] [varchar](255),
    [phonenumber] [varchar](15)
);