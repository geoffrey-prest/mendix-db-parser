USE [OnlineBookStore];

/**** Lorem ipsum dolor 234 #$% ****/

CREATE TABLE [dbo].[fulfillmentmanagement$shippingdetail] (
    [id] [int] PRIMARY KEY,
    [shippingaddress] [varchar](255),
    [shippingdate] [datetime],
    [deliverydate] [datetime],
    [shippingstatus] [varchar](50)
);