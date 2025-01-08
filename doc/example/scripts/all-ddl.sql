CREATE DATABASE [OnlineBookStore];

CREATE TABLE [dbo].[productmanagement$author] (
    [id] [int] PRIMARY KEY,
    [name] [varchar](100) NOT NULL,
    [bio] [text]
);

CREATE TABLE [dbo].[productmanagement$book] (
    [id] [int] PRIMARY KEY,
    [title] [varchar](255) NOT NULL,
    [price] [decimal](10, 2),
    [publicationyear] [year]
);

CREATE TABLE [dbo].[productmanagement$publisher] (
    [id] [int] PRIMARY KEY,
    [name] [varchar](100) NOT NULL,
    [address] [varchar](255)
);

CREATE TABLE [dbo].[customermanagement$customer] (
    [id] [int] PRIMARY KEY,
    [name] [varchar](100) NOT NULL,
    [email] [varchar](100) UNIQUE,
    [passwordhash] [varchar](255) NOT NULL,
    [address] [varchar](255),
    [phonenumber] [varchar](15)
);

CREATE TABLE [dbo].[ordermanagement$order] (
    [id] [int] PRIMARY KEY,
    [orderdate] [datetime],
    [totalamount] [decimal](10, 2),
    [paymentstatus] [varchar](50)
);

CREATE TABLE [dbo].[ordermanagement$orderitem] (
    [id] [int] PRIMARY KEY,
    [quantity] [int],
    [price] [decimal](10, 2)
);

CREATE TABLE [dbo].[productmanagement$category] (
    [id] [int] PRIMARY KEY,
    [categoryname] [varchar](100) NOT NULL
);

CREATE TABLE [dbo].[productmanagement$review] (
    [id] [int] PRIMARY KEY,
    [rating] [int] CHECK ([rating] BETWEEN 1 AND 5),
    [comment] [text],
    [reviewdate] [datetime]
);

CREATE TABLE [dbo].[fulfillmentmanagement$payment] (
    [id] [int] PRIMARY KEY,
    [paymentdate] [datetime],
    [amount] [decimal](10, 2),
    [paymentmethod] [varchar](50)
);

CREATE TABLE [dbo].[fulfillmentmanagement$shippingdetail] (
    [id] [int] PRIMARY KEY,
    [shippingaddress] [varchar](255),
    [shippingdate] [datetime],
    [deliverydate] [datetime],
    [shippingstatus] [varchar](50)
);

CREATE TABLE [dbo].[productmanagement$author_book] (
    [productmanagement$authorid] [int],
    [productmanagement$bookid] [int]
);

CREATE TABLE [dbo].[productmanagement$book_publisher] (
    [productmanagement$bookid] [int],
    [productmanagement$publisherid] [int]
);

CREATE TABLE [dbo].[productmanagement$book_category] (
    [productmanagement$bookid] [int],
    [productmanagement$categoryid] [int]
);

CREATE TABLE [dbo].[ordermanagement$order_customer] (
    [ordermanagement$orderid] [int],
    [customermanagement$customerid] [int]
);

CREATE TABLE [dbo].[ordermanagement$order_orderitem] (
    [ordermanagement$orderid] [int]
    [ordermanagement$orderitemid] [int]
);

CREATE TABLE [dbo].[ordermanagement$orderitem_book] (
    [ordermanagement$orderitemid] [int],
    [productmanagement$bookid] [int]
);

CREATE TABLE [dbo].[productmanagement$book_review] (
    [productmanagement$bookid] [int],
    [productmanagement$reviewid] [int]    
);

CREATE TABLE [dbo].[customermanagement$customer_review] (
    [customermanagement$customerid] [int],
    [productmanagement$reviewid] [int]
);

CREATE TABLE [dbo].[fulfillmentmanagement$payment_order] (
    [fulfillmentmanagement$paymentid] [int],
    [ordermanagement$orderid] [int]
);

CREATE TABLE [dbo].[fulfillmentmanagement$shippingdetail_order] (
    [fulfillmentmanagement$shippingid] [int],
    [ordermanagement$orderid] [int]
);
