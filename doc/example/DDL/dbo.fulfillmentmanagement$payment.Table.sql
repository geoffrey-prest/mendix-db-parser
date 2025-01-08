USE [OnlineBookStore];

/**** Lorem ipsum dolor 234 #$% ****/

CREATE TABLE [dbo].[fulfillmentmanagement$payment] (
    [id] [int] PRIMARY KEY,
    [paymentdate] [datetime],
    [amount] [decimal](10, 2),
    [paymentmethod] [varchar](50)
);