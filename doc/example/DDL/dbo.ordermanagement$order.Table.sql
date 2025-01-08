USE [OnlineBookStore];

/**** Lorem ipsum dolor 234 #$% ****/

CREATE TABLE [dbo].[ordermanagement$order] (
    [id] [int] PRIMARY KEY,
    [orderdate] [datetime],
    [totalamount] [decimal](10, 2),
    [paymentstatus] [varchar](50)
);